from copy import deepcopy
from unittest import TestCase
from unittest.mock import patch, Mock, ANY

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

    def test_run(self):
        count = 5
        events = [{}] * count
        long_poller_mock = Mock(return_value=events)
        long_poller_listen_mock = Mock()
        long_poller_listen_mock.listen = long_poller_mock
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

    ]
    EXPECTED_OUTPUTS = [
        START_TEXT,
        settings_dispatcher.INTENTS[1]["answer"],
        "Город отправления принят 'Москва'. Введите город назначения.",
        "Город назначения принят 'Санкт-Петербург'. Введите дату отправления.",

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
        assert send_mock.call_count == len(self.INPUTS)+1

        real_outputs = []
        for call in send_mock.call_args_list:
            args, kwargs = call
            real_outputs.append(kwargs["message"])


        for i in range(len(self.INPUTS)+1):
            print("*"*70)
            print(real_outputs[i])
            print(self.EXPECTED_OUTPUTS[i])
            print(real_outputs[i]==self.EXPECTED_OUTPUTS[i])


        assert real_outputs == self.EXPECTED_OUTPUTS