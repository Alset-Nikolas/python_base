# -*- coding: utf-8 -*-

# В очередной спешке, проверив приложение с прогнозом погоды, вы выбежали
# навстречу ревью вашего кода, которое ожидало вас в офисе.
# И тут же день стал хуже - вместо обещанной облачности вас встретил ливень.

# Вы промокли, настроение было испорчено, и на ревью вы уже пришли не в духе.
# В итоге такого сокрушительного дня вы решили написать свою программу для прогноза погоды
# из источника, которому вы доверяете.

# Для этого вам нужно:

# Создать модуль-движок с классом WeatherMaker, необходимым для получения и формирования предсказаний.
# В нём должен быть метод, получающий прогноз с выбранного вами сайта (парсинг + re) за некоторый диапазон дат,
# а затем, получив данные, сформировать их в словарь {погода: Облачная, температура: 10, дата:datetime...}
import argparse
import datetime
import math
import os
import requests
from bs4 import BeautifulSoup
from translate import Translator
import cv2
import peewee
import os.path

from WeatherMaker import WeatherMaker

from ImageMaker import ImageMaker

from Weather_BD import Weather_BD

from DatabaseUpdater import DatabaseUpdater

# Добавить класс ImageMaker.
# Снабдить его методом рисования открытки
# (использовать OpenCV, в качестве заготовки брать lesson_016/python_snippets/external_data/probe.jpg):
#   С текстом, состоящим из полученных данных (пригодится cv2.putText)
#   С изображением, соответствующим типу погоды
# (хранятся в lesson_016/python_snippets/external_data/weather_img ,но можно нарисовать/добавить свои)
#   В качестве фона добавить градиент цвета, отражающего тип погоды
# Солнечно - от желтого к белому+
# Дождь - от синего к белому
# Снег - от голубого к белому+
# Облачно - от серого к белому


'''
parser = argparse.ArgumentParser(description='Ping script')

parser.add_argument('--start_range_date', action="store", dest='start_range_date', help='Например 28.09.2020',
                    default='28.09.2020')
parser.add_argument('--last_range_date', action="store", dest='last_range_date', help="Например 28.09.2020",
                    default='30.09.2020')

args = parser.parse_args('--start_range_date 28.09.2020 --last_range_dat 30.09.2020'.split())
'''

# TODO всё взаимоотношение между классами надо перенести в этот общий метод
class Main:
    def __init__(self):
        pass

    def create_bd(self):  # TODO такая проверка и создание уже есть, дублировать её не нужно
        if not os.path.exists("DateBase.db"):
            print("Создали БД! Теперь есть прогнозы на 10 дней")
            WeatherMaker().run()
        else:
            print("БД уже есть!")

    def add_new_day(self, day, weather, temperature):
        print("\tДобавим новый день!")
        # TODO Запись данных надо организовывать в соответственном классе
        # TODO Тут просто получить данные из одного места и передать их классу который работает с БД
        try:
            probe = Weather_BD.get(Weather_BD.date == day)
            probe.weather = weather
            probe.temperature = temperature
            probe.save()
            print('Обновил ', day)
        except:
            new_day = Weather_BD.create(date=day, weather=weather, temperature=temperature)
            new_day.save()
            print('Добавил ', new_day)

    def show_all(self):
        DatabaseUpdater(start_range_date='28.09.0001', last_range_date='28.09.9999').run()

    def show_day(self, day):
        print('\t Посмотрим на день!')
        try:
            probe = Weather_BD.get(Weather_BD.date == day)
            print(f'{probe.date} \tПогода: {probe.weather} Температура: {probe.temperature}')

        except:

            print('В базе нет такого дня! ', day)

    def pictures_in_range_date(self, start_range_date, last_range_date):
        print('\tДелаем картинки')
        start_range_date = datetime.datetime.strptime(start_range_date, '%d.%m.%Y').date()
        last_range_date = datetime.datetime.strptime(last_range_date, '%d.%m.%Y').date()
        # TODO И селект отсюда использовать не нужно
        # TODO все эти действия должны быть реализованы в классе по работе с БД
        # TODO и уже там надо сделать селект и вернуть итоговый набор данных
        # TODO а тут просто передать его ImageMaker-у
        for weather in Weather_BD.select():
            if start_range_date <= datetime.datetime.strptime(weather.date, '%d.%m.%Y').date() <= last_range_date:
                ImageMaker(day=weather.date).run()

    def schow_in_range_date(self, start_range_date, last_range_date):
        DatabaseUpdater(start_range_date=start_range_date, last_range_date=last_range_date).run()


# TODO Весь этот код с циклом и прочим надо добавить в класс, в main например
while True:
    A = Main()
    print()
    print('=' * 30)
    print("1 - Проверить наличие БД")
    print("2 - Посмотреть всю БД")
    print("3 - Показать в диапазоне дат все данные")
    print("4 - Показать картинки с погодой в диапазоне дат")
    print("q - Выход")
    print('=' * 30)
    N = input()
    if N not in ('q', '1', '2', '3', '4'):
        print("Такого варианта нет!")
        continue
    if N == 'q':
        break
        # TODO При вызове этого метода нужно гарантировать, что все финализаторы всяких объектов отработают.
        # TODO Это прокатит при их вызове в __del__, но не везде это возможно.
        # TODO Старайтесь избегать вызова exit, давайте программе штатно завершиться
    elif N == '1':
        A.create_bd()  # TODO в идеале все действия собрать в словарь и вызывать их по ключу
        # TODO чтобы избваиться от множества сравнений подобных
        # TODO Названия действий тоже можно в этот словарь сложить и оттуда печать вести, вместо строк 427-434
    elif N == '2':
        A.show_all()
    elif N == '3':
        while True:
            print('Пример 20.09.2020')
            start = input("Введите с какой даты хотите смотреть = ")
            last = input("До какой = ")
            try:
                A.schow_in_range_date(start, last)
                break
            except:
                print("Данные в другом фармате!")
    elif N == '4':
        while True:
            print('Пример 20.09.2020')
            start = input("Введите с какой даты хотите смотреть = ")
            last = input("До какой = ")
            try:
                A.pictures_in_range_date(start, last)
                break
            except:
                print("Данные в другом фармате!")

# Добавить класс DatabaseUpdater с методами:
#   Получающим данные из базы данных за указанный диапазон дат.
#   Сохраняющим прогнозы в базу данных (использовать peewee)

# Сделать программу с консольным интерфейсом, постаравшись все выполняемые действия вынести в отдельные функции.
# Среди действий, доступных пользователю, должны быть:
#   Добавление прогнозов за диапазон дат в базу данных+
#   Получение прогнозов за диапазон дат из базы+
#   Создание открыток из полученных прогнозов+
#   Выведение полученных прогнозов на консоль+
# При старте консольная утилита должна загружать прогнозы за прошедшую неделю.

# Рекомендации:
# Можно создать отдельный модуль для инициализирования базы данных.
# Как далее использовать эту базу данных в движке:
# Передавать DatabaseUpdater url-путь
# https://peewee.readthedocs.io/en/latest/peewee/playhouse.html#db-url
# Приконнектится по полученному url-пути к базе данных
# Инициализировать её через DatabaseProxy()
# https://peewee.readthedocs.io/en/latest/peewee/database.html#dynamically-defining-a-database
