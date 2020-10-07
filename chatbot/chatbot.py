# -*- coding: utf-8 -*-
from random import randint
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import logging

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


class Bot:
    '''
    Echo bot vk.com.

    Use python 3.7
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
        if event.type == VkBotEventType.MESSAGE_NEW:
            log.debug("отправляем сообщение назад")
            self.api.messages.send(
                message=event.object['message']['text'],
                random_id=randint(0, 2 ** 20),
                peer_id=event.object['message']['peer_id']
            )
        else:
            log.info('не умею обрабатывать %s', event.type)


if __name__ == '__main__':
    configure_logging()
    bot = Bot(token=settings.TOKEN, group_id=settings.GROUP_ID)
    bot.run()
