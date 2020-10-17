import datetime
from random import randint
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import logging
from bot_dispatcher import handlers_dispatcher, settings_dispatcher
log = logging.getLogger('bot_dispatcher')



def configure_logging():
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    stream_handler.setLevel(logging.INFO)
    log.addHandler(stream_handler)

    file_handler = logging.FileHandler("../chatbot/bot.log", encoding='UTF-8', mode='w')
    file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    file_handler.setLevel(logging.DEBUG)
    log.addHandler(file_handler)

    log.setLevel(logging.DEBUG)


try:
    pass
except ImportError as er:
    print(er)
    exit("DO cp settings_dispatcher.py.default settings_dispatcher.py and set token!")


class UserState:
    """ Состояние пользователя внутри сценария"""

    def __init__(self, scenario_name, step_name, context=None):
        self.scenario_name = scenario_name
        self.step_name = step_name
        self.context = context or {"departure_city": None, "arrival_city": None,
                                   "date": None, "flight": None, "comment": None,
                                   "right": None, "telephone": None, "var": ""}


START_TEXT = """
=============================
Вас приветствует Диспетчер!\n
Укажите город из которого вы хотите улететь!\n
Или воспольззуйтесь командой /help, чтобы просмотреть весь сценарий\n
Если вы ошиблись введите /ticket и регистрация начнется сначала\n
=============================
"""


class Bot:
    '''
    bot Диспетчер  vk.com.
    Use python 3.7

    Поддерживаем ответы на вопросы:
    - /help
    - /ticket
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
        self.DATE = settings_dispatcher.DATE

    def run(self):
        '''Запуск бота.'''
        if __name__ == "__main__":
            vk_session = vk_api.VkApi(token=settings_dispatcher.TOKEN)
            vk = vk_session.get_api()
            chat_id = vk.messages.searchConversations()["items"][0]["peer"]["local_id"]
            start_text = START_TEXT
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


        text_to_send = ''
        if event.type != VkBotEventType.MESSAGE_NEW:
            log.info('не умею обрабатывать %s', event.type)
            return
        user_id = event.object['message']['peer_id']
        text = event.obj['message']["text"]

        for intent in settings_dispatcher.INTENTS:
            log.debug(f"User gets {intent}")
            if any(token in text.lower() for token in intent["tokens"]):
                # run intent
                if intent["tokens"] in text.lower() or text.lower()[1:] in intent["tokens"][1:]:
                    if intent["answer"]:
                        #print("intent['answer']")
                        text_to_send = intent["answer"]
                        break
                    else:
                        self.start_scenario(user_id)
                        text_to_send = '==Start==\nВас приветствует Диспетчер! Введите город отправления:\n'
                        break
            else:

                if user_id not in self.user_states:
                    self.start_scenario(user_id)
                    #print("user_id not in")

                text_to_send = self.continue_scenario(user_id, text)
                break
        self.api.messages.send(
            message=text_to_send,
            random_id=randint(0, 2 ** 20),
            peer_id=event.object['message']['peer_id']
        )

    def start_scenario(self, user_id):
        scanerio_name = "registration"
        scanerio = settings_dispatcher.SCENARIOS[scanerio_name]
        first_step = scanerio["first_step"]
        self.user_states[user_id] = UserState(scenario_name=scanerio_name, step_name=first_step)

    def continue_scenario(self, user_id, text):
        state = self.user_states[user_id]
        #print(state.context)

        steps = settings_dispatcher.SCENARIOS[state.scenario_name]["steps"]
        step = steps[state.step_name]

        handler = getattr(handlers_dispatcher, step["handler"])
        #print("handler = ", handler(text=text, context=state.context))

        if handler(text=text, context=state.context):
            # next step
            text_to_send = step["text"]

            if state.step_name == "step3":
                otvet = []
                date  = datetime.datetime.strptime(state.context["date"], '%d-%m-%Y').date()
                for line in self.DATE:

                    date_in_line = line["date"]
                    if date_in_line >= date and line["departure_city"] == state.context["departure_city"] and line[
                        "arrival_city"] == state.context["arrival_city"]:
                        otvet.append([line["date"], line['fly_time'], line['flight number'], line['free places']])
                if len(otvet) == 0:
                    text = 'Нет таких рейсов!\n\n'
                    self.user_states.pop(user_id)
                    text += START_TEXT
                    text_to_send = text
                else:
                    text = 'Варианты:\n'
                    for line in otvet:
                        text += f'{line[0]} в {line[1]} номер рейса {line[2]} свободных мест {line[3]}\n'
                    text_to_send += text
                    text_to_send += "Укажите номер рейса!\n"

            if state.step_name == "step6":
                if not state.context["right"]:
                    step["next_step"] = None
                    self.user_states.pop(user_id)
                    text += 'Вас приветствует Диспетчер! Введите город отправления:'
                    text_to_send += text

            if step["next_step"]:
                # switch to next step
                state.step_name = step["next_step"]


        else:
            # retry current step
            text_to_send = step["failure_text"]

        #print(state.step_name, '--->', text_to_send)
        return text_to_send.format(**state.context)


if __name__ == '__main__':
    configure_logging()
    bot = Bot(token=settings_dispatcher.TOKEN, group_id=settings_dispatcher.GROUP_ID)
    bot.run()
