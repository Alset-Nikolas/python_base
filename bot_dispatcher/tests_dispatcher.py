import datetime
from copy import deepcopy
from unittest import TestCase
from unittest.mock import patch, Mock, ANY, MagicMock

from vk_api.bot_longpoll import VkBotMessageEvent
from vk_api import VkApi
import settings_dispatcher
from Bot_Dispatcher import Bot, START_TEXT

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
    DATE = [{'arrival_city': 'Москва',
             'date': datetime.date(2020, 10, 16),
             'departure_city': 'Санкт-Петербург',
             'flight number': 3546,
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
        "16-10-2020",
        "3546",
        "ФФФФФ",
        "да",
        "88888888888",

    ]
    EXPECTED_OUTPUTS = [
        settings_dispatcher.INTENTS[1]["answer"],
        "Город отправления принят 'Москва'. Введите город назначения.",
        "Город назначения принят 'Санкт-Петербург'. Введите дату отправления.",

        """Будем искать билеты на '16-10-2020'.
Варианты:
2020-10-15 в 19.00 номер рейса 3546 свободных мест 3
Укажите номер рейса!""",

        "Выбор рейса 3546.Предлагаем написать комментарий в произвольной форме.",

        """Спасибо за комментарий! ФФФФФ.
Уточняем введенные данные.
Москва —> Санкт-Петербург 14-10-2020 рейс 3546!
да или нет?"""
        
        "Супер! Введите номер телефона",

        """Мы будем звонить на 88888888888.\n
Спасибо за регистрацию!\n
Если хотите заказать еще один билет Введите город отправления:"""

    ]

    def test_run_ok(self):

        send_mock = Mock()
        api_mock = Mock()
        api_mock.messages.send = send_mock


        events = []
        for input_text in self.INPUTS:
            event = deepcopy(self.RAW_EVENT)
            event["object"]['message']["text"] = input_text
            events.append(VkBotMessageEvent(event))

        long_poller_mock = Mock()
        long_poller_mock.listen = Mock(return_value=events)



        settings_dispatcher_mock = MagicMock()
        settings_dispatcher_mock.DATE = MagicMock()
        settings_dispatcher_mock.INTENTS = MagicMock()
        settings_dispatcher_mock.SCENARIOS = MagicMock()
        settings_dispatcher_mock.DATE.__iter__.return_value = self.DATE
        settings_dispatcher_mock.INTENTS.__iter__.return_value = settings_dispatcher.INTENTS
        settings_dispatcher_mock.SCENARIOS.__iter__.return_value = settings_dispatcher.SCENARIOS

        for x in settings_dispatcher_mock.DATE:
            print(x)
        with patch("Bot_Dispatcher.settings_dispatcher", settings_dispatcher_mock):
            with patch("Bot_Dispatcher.VkBotLongPoll", return_value=long_poller_mock):
                bot = Bot("", "")
                bot.api = api_mock
                bot.run()
            print("===============")
            print(send_mock)
            print("===============")
            print(self.INPUTS)
            print("===============")
            print(send_mock.call_count, len(self.INPUTS))
            assert send_mock.call_count == len(self.INPUTS)

            real_outputs = []
            for call in send_mock.call_args_list:
                args, kwargs = call
                print(call)
                real_outputs.append(kwargs["message"])

            for i in range(len(self.INPUTS)-1):
                if real_outputs[i]!=self.EXPECTED_OUTPUTS[i]:
                    pass
                    '''print("=-="*70)
                    print(real_outputs[i])
                    print("&=&" * 70)
                    print(self.EXPECTED_OUTPUTS[i])
                    print("=-="*70)'''


            assert real_outputs == self.EXPECTED_OUTPUTS

    def test_change_date(self):
        print(len(settings_dispatcher.DATE))
        with patch('settings_dispatcher.DATE', [1,2,3]):
            print(settings_dispatcher.DATE, len(settings_dispatcher.DATE))