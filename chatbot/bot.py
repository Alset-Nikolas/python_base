# -*- coding: utf-8 -*-
from random import randint
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import logging
import handlers

log = logging.getLogger('bot')


def configure_logging():
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    stream_handler.setLevel(logging.INFO)
    log.addHandler(stream_handler)

    file_handler = logging.FileHandler("bot.log", encoding='UTF-8', mode='w')
    file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    file_handler.setLevel(logging.DEBUG)
    log.addHandler(file_handler)

    log.setLevel(logging.DEBUG)


try:
    import settings
except ImportError as er:
    print(er)
    exit("DO cp settings.py.default settings.py and set token!")


class UserState:
    """ Состояние пользователя внутри сценария"""

    def __init__(self, scenario_name, step_name, context=None):
        self.scenario_name = scenario_name
        self.step_name = step_name
        self.context = context or {"name": None, "email": None}


class Bot:
    '''
    Echo bot vk.com.
    Use python 3.7

    Поддерживаем ответы на вопросы про дату, место проведения и сценарий регистрации:
    - спрашиваем имя
    - спрашиваем email
    - говорим об успешной регистрации
    Если шаг не пройден, задаеи уточняюший вопрос пока шаг не будудет пройден.
    '''

    def __init__(self, token, group_id):
        """
        :param group_id: group id из группы vk
        :param token: секретный токен
        """
        self.token = token
        self.group_id = group_id
        self.vk = vk_api.VkApi(token=self.token)
        self.long_poller = VkBotLongPoll(vk=self.vk, group_id=self.group_id)
        self.api = self.vk.get_api()
        self.user_states = dict()  # user_id --> UserState

    def run(self):
        '''Запуск бота.'''
        for event in self.long_poller.listen():
            log.debug("полученло событие")
            try:
                self.on_event(event)
            except Exception:
                log.exception('Ошибка в обработке события:')

    def on_event(self, event):
        '''Отправляет сообщение назад, если это текст.
        :param event: VkBotMessageEvent
        '''
        if event.type != VkBotEventType.MESSAGE_NEW:
            log.info('не умею обрабатывать %s', event.type)
            return
        user_id = event.object['message']['peer_id']
        text = event.obj['message']["text"]
        if user_id in self.user_states:
            # continue scenario
            text_to_send = self.continue_scenario(user_id, text=text)

        else:
            # serch intent
            print(self.user_states)
            for intent in settings.INTENTS:
                log.debug(f"User gets {intent}")
                if any(token in text.lower() for token in intent["tokens"]):
                    # run intent
                    if intent["answer"]:
                        text_to_send = intent["answer"]
                    else:
                        text_to_send = self.start_scenario(user_id, intent["scenario"])
                    break
            else:
                text_to_send = settings.DEFAULT_ANSWER
        print(text_to_send)
        self.api.messages.send(
            message=text_to_send,
            random_id=randint(0, 2 ** 20),
            peer_id=event.object['message']['peer_id']
        )

    def start_scenario(self, user_id, scanerio_name):
        scanerio = settings.SCENARIOS[scanerio_name]
        first_step = scanerio["first_step"]
        step = scanerio["steps"][first_step]
        text_to_send = step["text"]
        self.user_states[user_id] = UserState(scenario_name=scanerio_name, step_name=first_step)
        return text_to_send

    def continue_scenario(self, user_id, text):
        state = self.user_states[user_id]
        steps = settings.SCENARIOS[state.scenario_name]["steps"]
        step = steps[state.step_name]

        handler = getattr(handlers, step["handler"])
        if handler(text=text, context=state.context):
            # next step
            next_step = steps[step["next_step"]]
            text_to_send = next_step["text"].format(**state.context)

            if next_step["next_step"]:
                # switch to next step
                state.step_name = step["next_step"]
            else:
                # finish scenario
                self.user_states.pop(user_id)
                log.info("Заргеистрирован {name} , {email}".format(**state.context))
        else:
            # retry current step
            text_to_send = step["failure_text"].format(**state.context)
        return text_to_send


if __name__ == '__main__':
    configure_logging()
    bot = Bot(token=settings.TOKEN, group_id=settings.GROUP_ID)
    bot.run()
