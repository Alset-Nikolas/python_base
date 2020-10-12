import datetime
from random import randint
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import logging
import handlers_dispatcher

log = logging.getLogger('bot_dispatcher')


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
    import settings_dispatcher
except ImportError as er:
    print(er)
    exit("DO cp settings_dispatcher.py.default settings_dispatcher.py and set token!")

class UserState:
    """ Состояние пользователя внутри сценария"""

    def __init__(self, scenario_name, step_name, context=None):
        self.scenario_name = scenario_name
        self.step_name = step_name
        self.context = context or {"departure_city": None, "arrival_city": None,
                                   "date": None, "flight": None, "comment": None}


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
        vk_session = vk_api.VkApi(token=settings_dispatcher.TOKEN)
        vk = vk_session.get_api()
        chat_id = vk.messages.searchConversations()["items"][0]["peer"]["local_id"]
        start_text = "Вас приветствует Диспетчер! Введите город отправления:"
        self.api.messages.send(
            message=start_text,
            random_id=randint(0, 2 ** 20),
            peer_id=chat_id
        )

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

            for intent in settings_dispatcher.INTENTS:
                log.debug(f"User gets {intent}")
                if any(token in text.lower() for token in intent["tokens"]):
                    # run intent
                    if intent["answer"]:
                        text_to_send = intent["answer"]
                    else:
                        text_to_send = self.start_scenario(user_id, intent["scenario"])
                    break
            else:
                text_to_send = self.start_scenario(user_id, text)

        self.api.messages.send(
            message=text_to_send,
            random_id=randint(0, 2 ** 20),
            peer_id=event.object['message']['peer_id']
        )


    def start_scenario(self, user_id, text):
        scanerio_name = "registration"
        scanerio = settings_dispatcher.SCENARIOS[scanerio_name]
        first_step = scanerio["first_step"]
        step = scanerio["steps"][first_step]
        text_to_send = step["text"]
        self.user_states[user_id] = UserState(scenario_name=scanerio_name, step_name=first_step)
        self.user_states[user_id].context["departure_city"]=text
        self.user_states[user_id].step_name = step["next_step"]
        return text_to_send.format(**self.user_states[user_id].context)

    def continue_scenario(self, user_id, text):
        print("=========================")
        state = self.user_states[user_id]
        print(state.context)

        steps = settings_dispatcher.SCENARIOS[state.scenario_name]["steps"]
        step = steps[state.step_name]
        print(state.step_name)

        handler = getattr(handlers_dispatcher, step["handler"])


        if handler(text=text, context=state.context):
            # next step

            text_to_send = step["text"]
            if step["next_step"]:
                # switch to next step
                state.step_name = step["next_step"]
            else:
                # finish scenario
                self.user_states.pop(user_id)
                log.info("Заргеистрирован {name} , {email}".format(**state.context))
        else:
            # retry current step
            text_to_send = step["failure_text"]
        print(state.context)
        otvet = []
        text = ''

        if state.step_name =="step4":
            date = datetime.datetime.strptime(state.context["date"], '%d-%m-%Y').date()
            for line in settings_dispatcher.DATE:
                date_in_line = line["date"]
                if date_in_line >= date and line["departure_city"]==state.context["departure_city"] and line["arrival_city"]==state.context["arrival_city"]:
                    otvet.append([line["date"], line['fly_time'], line['flight number'], line['free places']])

            if len(otvet) == 0:
                text ='Нет таких рейсов!\n\n'
                step["next_step"] = None
                self.user_states.pop(user_id)
                text += 'Вас приветствует Диспетчер! Введите город отправления:'
            else:
                text = 'Варианты:\n'
                for line in otvet:
                    text += f'{line[0]} в {line[1]} номер рейса {line[2]} свободных мест {line[3]}\n'
                text_to_send += text
                text_to_send +="Укажите номер рейса!\n"

        return text_to_send.format(**state.context)


if __name__ == '__main__':
    configure_logging()
    bot = Bot(token=settings_dispatcher.TOKEN, group_id=settings_dispatcher.GROUP_ID)
    bot.run()
