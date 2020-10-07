from copy import deepcopy
from unittest import TestCase
from unittest.mock import patch, Mock, ANY

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api import VkApi
import settings
from bot import Bot


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
        with patch("VkApi"):  # TODO в патче нужно указать что именно вы хотите заменить
            # TODO если просто указать VkApi - то он будет пытаться заменить этот VkApi тут
            # TODO а нам надо заменить его в модуле chatbot (или bot) при этом не просто VkApi
            # TODO а vk_api.VkApi, т.к. мы не импортируем его напрямую, а используем из этой библиотеки
            # TODO ниже в комментах у вас правильные пути добавлены, насколько я вижу
            with patch("VkBotLongPoll", return_value=long_poller_listen_mock):
                bot = Bot("", "")
                bot.on_event = Mock()
                bot.run()
                bot.on_event.assert_called_with({})
                assert bot.on_event.call_count == count

    '''
    def test_on_event(self):
        event = VkBotMessageEvent(raw=self.RAW_EVENT)
        send_mock = Mock()
        with patch("chatbot.vk_api.VkApi"):
            with patch("chatbot.VkBotLongPoll"):
                bot=Bot("","")
                bot.api = Mock()
                bot.api.messages.send = send_mock
                bot.on_event(event=event)
        send_mock.assert_called_once_with(
            message=self.RAW_EVENT["object"]["message"]["text"],
            random_id=ANY,
            peer_id=self.RAW_EVENT["object"]["message"]["peer_id"]
        )'''

    INPUTS = [
        "Привет",
        "А когда?",
        "Где будет конференция?",
        "Зарегистрируй меня",
        "Вениамин",
        "мой адрес email@email",
        "email@email.ru"
    ]
    EXPECTED_OUTPUTS = [
        settings.DEFAULT_ANSWER,
        settings.INTENTS[0]["answer"],
        settings.INTENTS[1]["answer"],
        settings.SCENARIOS["registration"]["steps"]["step1"]["text"],
        settings.SCENARIOS["registration"]["steps"]["step2"]["text"],
        settings.SCENARIOS["registration"]["steps"]["step2"]["failure_text"],
        settings.SCENARIOS["registration"]["steps"]["step3"]["text"].format(name='Вениамин', email='email@email.ru'),
    ]

    def tust_run_ok(self):
        send_mock = Mock()
        api_mock = Mock()
        api_mock.message.send = send_mock
        # TODO в боте у вас есть метод self.api.messages.send
        # TODO если вы хотите заменить его, то надо указать не .message.send а .messages.send

        events = []
        for input_text in self.INPUTS:
            event = deepcopy(self.RAW_EVENT)
            event["object"]["text"] = input_text
            events.append(VkBotEvent(event))  # TODO тут нужен VkBotMessageEvent например
            # TODO from vk_api.bot_longpoll import VkBotMessageEvent, VkBotEvent -- сперва его стоит импортировать

        long_poller_mock = Mock()
        long_poller_mock.listen = Mock(return_value=events)

        with patch("bot.VkBotLongPoll", return_value=long_poller_mock):
            bot = Bot("", "")
            bot.api = api_mock
            bot.run()
        assert send_mock.call_count == len(self.INPUTS)

        real_outputs = []
        for call in send_mock.call_args_list:
            args, kwargs = call
            real_outputs.append(kwargs["mwssage"])
        for real, expec in zip(real_outputs, self.EXPECTED_OUTPUTS):
            print(real)
            print('-' * 50)
            print(expec)
            print('-' * 50)
            print(real == expec)
            print('_' * 50)
        assert real_outputs == self.EXPECTED_OUTPUTS
