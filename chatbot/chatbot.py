# -*- coding: utf-8 -*-

from random import randint
import vk_api
import vk_api.bot_longpoll
from _token import VK_TOKEN

group_id = 198507410


class Bot:

    def __init__(self, token, group_id):
        self.token = token
        self.group_id = group_id
        self.vk = vk_api.VkApi(token=self.token)
        self.long_poller = vk_api.bot_longpoll.VkBotLongPoll(vk=self.vk, group_id=self.group_id)
        self.api = self.vk.get_api()


    def run(self):
        for event in self.long_poller.listen():
            print('полученло событие')
            try:
                self.on_event(event)
            except Exception as err:
                print(err)
    def on_event(self, event):
        if event.type == vk_api.bot_longpoll.VkBotEventType.MESSAGE_NEW:
            print(event.object['message']['text'])
            print(event.object['message']['text'], randint(0, 2**20), type(event), event.obj.peer_id)
            self.api.messages.send(
                message=event.object['message']['text'],
                random_id=randint(0, 2**20),
                peer_id=event.obj.peer_id
            )
        else:
            print('не умею обрабатывать', event.type)


if __name__ == '__main__':
    bot = Bot(token=VK_TOKEN, group_id=group_id)
    bot.run()
