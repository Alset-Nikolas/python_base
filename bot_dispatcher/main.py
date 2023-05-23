import datetime
from random import randint

import requests
import vk_api
from pony.orm import db_session
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import logging
from app import handlers_dispatcher, settings_dispatcher
from app.models_dispatcher import UserState, Registration

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


'''
class UserState:
    """ Состояние пользователя внутри сценария"""

    def __init__(self, scenario_name, step_name, context=None):
        self.scenario_name = scenario_name
        self.step_name = step_name
        self.context = context or {"departure_city": None, "arrival_city": None,
                                   "date": None, "flight": None, "comment": None,
                                   "right": None, "telephone": None, "var": ""}
'''


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
        #self.user_states = dict()  # user_id --> UserState
        self.DATE = settings_dispatcher.DATE

    def run(self):
        '''Запуск бота.'''
        for event in self.long_poller.listen():
            log.debug("полученло событие")
            try:
                self.on_event(event)
            except Exception:
                log.exception('Ошибка в обработке события:')

    @db_session
    def on_event(self, event):

        text_to_send = ''
        if event.type != VkBotEventType.MESSAGE_NEW:
            log.info('не умею обрабатывать %s', event.type)
            return
        user_id = event.object['message']['peer_id']
        text = event.obj['message']["text"]
        #print("Пришло", text)
        state = UserState.get(user_id=str(user_id))
        if state is not None:
            # continue scenario
            text_to_send = self.continue_scenario(text=text, state=state,user_id=user_id)
        else:
        # serch intent
            for intent in settings_dispatcher.INTENTS:
                log.debug(f"User gets {intent}")
                if any(token in text.lower() for token in intent["tokens"]):
                    # run intent
                    if intent["tokens"] in text.lower() or text.lower()[1:] in intent["tokens"][1:]:
                        if intent["answer"]:
                            # print("intent['answer']")
                            text_to_send = intent["answer"]
                            break
                        else:
                            self.start_scenario(user_id)
                            text_to_send = '==Start==\nВас приветствует Диспетчер! Введите город отправления:\n'
                            break
                else:
                        self.start_scenario(user_id)
                        state = UserState.get(user_id=str(user_id))
                        #print("on_event state.context = ", state.context)
                        text_to_send = self.continue_scenario(text=text, state=state,user_id=user_id)
                        break
            #print("text_to_send=", text_to_send)
        self.api.messages.send(
            message=text_to_send,
            random_id=randint(0, 2 ** 20),
            peer_id=event.object['message']['peer_id']
        )

    def start_scenario(self, user_id):
        scanerio_name = "registration"
        scanerio = settings_dispatcher.SCENARIOS[scanerio_name]
        first_step = scanerio["first_step"]
        UserState(user_id=str(user_id), scenario_name=scanerio_name, step_name=first_step, context={})



    def continue_scenario(self, text, state,user_id):

        #print("continue_scenario state.context=", state.context)

        steps = settings_dispatcher.SCENARIOS[state.scenario_name]["steps"]
        step = steps[state.step_name]

        handler = getattr(handlers_dispatcher, step["handler"])
        #print("continue_scenario handler = ", handler(text=text, context=state.context))

        if handler(text=text, context=state.context):
            # next step
            text_to_send = step["text"]

            if handler(text=text, context=state.context) not in [True, False]:
                text_to_send += handler(text=text, context=state.context)

            if state.step_name == "step6":
                if not state.context["right"]:
                    step["next_step"] = None
                    state.delete()
                    #print("Удаляем из базы")
                    text += 'Вас приветствует Диспетчер! Введите город отправления:'
                    text_to_send += text

            if step["next_step"]:
                # switch to next step
                state.step_name = step["next_step"]
            else:
                #print("state.context=", state.context)
                #print("state.context['departure_city']", state.context["departure_city"])
                Registration(user_id=str(user_id),
                             departure_city=state.context["departure_city"],
                             arrival_city=state.context["arrival_city"],
                             date=state.context["date"],
                             flight=state.context["flight"],
                             comment=state.context["comment"],
                             telephone=state.context["telephone"])
                handler = getattr(handlers_dispatcher, step["image"])
                image = handler(text, state.context)
                self.send_image(image, user_id)
                text = step["text"].format(**state.context)
                state.delete()
                print("Удаляем из базы")
                return text

        else:
            # retry current step
            text_to_send = step["failure_text"]
        return text_to_send.format(**state.context)

    def send_image(self, image, user_id):

        upload_url = self.api.photos.getMessagesUploadServer()["upload_url"]
        upload_date = requests.post(url=upload_url, files={"photo": ("image.png", image, "image/png")}).json()
        image_data = self.api.photos.saveMessagesPhoto(**upload_date)
        owner_id = image_data[0]["owner_id"]
        media_id = image_data[0]["id"]
        access_key = image_data[0]['access_key']
        attachment = f'photo{owner_id}_{media_id}_{access_key}'
        self.api.messages.send(
            attachment=attachment,
            random_id=randint(0, 2 ** 20),
            peer_id=user_id
        )

if __name__ == '__main__':
    configure_logging()
    bot = Bot(token=settings_dispatcher.TOKEN, group_id=settings_dispatcher.GROUP_ID)
    bot.run()
