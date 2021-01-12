import datetime
from copy import deepcopy
from unittest import TestCase
from unittest.mock import patch, Mock, ANY, MagicMock

from pony.orm import db_session, rollback
from vk_api.bot_longpoll import VkBotMessageEvent
from vk_api import VkApi
import settings_dispatcher
from Bot_Dispatcher import Bot, START_TEXT

date_now = datetime.datetime.now().date().strftime('%d-%m-%Y')



def isolate_db(test_func):
    def wrapper(*args, **kwargs):
        with db_session:
            test_func(*args, **kwargs)
            rollback()

    return wrapper




class Test1(TestCase):
    RAW_EVENT = {
        'type': 'message_new',
        'object': {'message': {'date': 1600102810, 'from_id': 548199338, 'id': 89, 'out': 0,
                               'peer_id': 548199338, 'text': 'м', 'conversation_message_id': 88,
                               'fwd_messages': [], 'important': False, 'random_id': 0, 'attachments': [],
                               'is_hidden': False},
                   'client_info': {'button_actions': ['text', 'vkpay', 'open_app', 'location', 'open_link'],
                                   'keyboard': True, 'inline_keyboard': True, 'carousel': False, 'lang_id': 0}},
        'group_id': 198507410, 'event_id': '7eaa4ff72c79d802328422c91cde763d6ee5b4a5'}
    DATE = [{'arrival_city': 'Санкт-Петербург',
             'date': datetime.datetime.now().date(),
             'departure_city': 'Москва',
             'flight number': "3546",
             'fly_time': '20.00',
             'free places': 3}]

    def test_run(self):
        count = 5
        events = [{}] * count
        long_poller_mock = Mock(return_value=events)
        long_poller_listen_mock = Mock()
        long_poller_listen_mock.listen = long_poller_mock

        settings_dispatcher_mock = Mock()
        settings_dispatcher_mock.DATE = MagicMock(return_value=self.DATE)
        settings_dispatcher_mock.INTENTS = settings_dispatcher.INTENTS
        settings_dispatcher_mock.SCENARIOS = settings_dispatcher.SCENARIOS

        with patch("Bot_Dispatcher.settings_dispatcher", return_value=settings_dispatcher_mock):
            with patch("Bot_Dispatcher.vk_api.VkApi"):
                with patch("Bot_Dispatcher.VkBotLongPoll", return_value=long_poller_listen_mock):
                    bot = Bot("", "")
                    bot.on_event = Mock()
                    bot.run()
                    bot.on_event.assert_called_with({})
                    assert bot.on_event.call_count == count

    INPUTS = [
        "/help",
        "москв",
        "питер",
        datetime.datetime.now().date().strftime('%d-%m-%Y'),
        "3546",
        "ФФФФФ",
        "да",
        "88888888888",

    ]
    EXPECTED_OUTPUTS = [
        settings_dispatcher.INTENTS[1]["answer"],
        "Город отправления принят 'Москва'. Введите город назначения.",
        "Город назначения принят 'Санкт-Петербург'. Введите дату отправления.",
        f"""Будем искать билеты на '{datetime.datetime.now().date().strftime('%d-%m-%Y')}'.
Варианты:
{datetime.datetime.now().date()} в 20.00 номер рейса 3546 свободных мест 3
Укажите номер рейса!
""",

        """Выбор рейса 3546.
Предлагаем написать комментарий в произвольной форме.""",

        f"""Спасибо за комментарий! ФФФФФ.
 Уточняем введенные данные.
 Москва --> Санкт-Петербург {datetime.datetime.now().date().strftime('%d-%m-%Y')} рейс 3546!
 да или нет?""",

        "Супер! Введите номер телефона",

        """Мы будем звонить на 88888888888.
Спасибо за регистрацию!
Если хотите заказать еще один билет Введите город отправления:"""
]

    @isolate_db
    def test_run_ok(self):

        send_mock = Mock()
        api_mock = Mock()
        api_mock.messages.send = send_mock

        events = []
        for input_text in self.INPUTS:
            event = deepcopy(self.RAW_EVENT)
            event["object"]['message']["text"] = input_text
            print(input_text)
            events.append(VkBotMessageEvent(event))

        long_poller_mock = Mock()
        long_poller_mock.listen = Mock(return_value=events)

        with patch("Bot_Dispatcher.settings_dispatcher.DATE", self.DATE):
            with patch("Bot_Dispatcher.handlers_dispatcher.DATE", self.DATE):
                with patch("Bot_Dispatcher.VkBotLongPoll", return_value=long_poller_mock):
                    with patch("Bot_Dispatcher.handlers_dispatcher.ALL_FLY_NUMBERS", {3546}):


                        bot = Bot("", "")
                        bot.send_image=Mock()
                        bot.api = api_mock
                        bot.run()
                    print(send_mock.call_count)
                    print(self.INPUTS)

                    assert send_mock.call_count == len(self.INPUTS)

                    real_outputs = []
                    for call in send_mock.call_args_list:
                        args, kwargs = call
                        real_outputs.append(kwargs["message"])

                    for i in range(len(self.INPUTS)):
                        try:
                            if real_outputs[i] != self.EXPECTED_OUTPUTS[i]:
                                print(i)
                                print("0" * 70)
                                print(real_outputs[i])
                                print("&=&" * 70)
                                print(self.EXPECTED_OUTPUTS[i])
                                print("0" * 70)
                        except:
                            if len(real_outputs)>len(self.EXPECTED_OUTPUTS):
                                print("Почему-то есть лишнее смс")
                                print(real_outputs[-1])
                            else:
                                print("Почему-то нет такого смс")
                                print(self.EXPECTED_OUTPUTS[-1])

                    assert real_outputs == self.EXPECTED_OUTPUTS

