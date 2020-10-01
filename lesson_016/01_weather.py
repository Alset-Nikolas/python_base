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
# from translate import Translator
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


class Main:
    def __init__(self):
        self.matrix_weather = WeatherMaker().run()
        self.Weather_BD = Weather_BD
        self.DatabaseUpdater = DatabaseUpdater
        self.ImageMaker = ImageMaker

    def add_new_day(self, day, weather, temperature):
        print("\tДобавим новый день!")
        self.DatabaseUpdater.add_new_day(day=day, weather=weather, temperature=temperature)

    def show_all(self):
        self.DatabaseUpdater(start_range_date='28.09.0001', last_range_date='28.09.9999',
                             matrix_weather=self.matrix_weather).run()

    def show_day(self, day):
        print('\t Посмотрим на день!')
        try:
            probe = self.Weather_BD.get(Weather_BD.date == day)
            print(f'{probe.date} \tПогода: {probe.weather} Температура: {probe.temperature}')
        except:
            print('В базе нет такого дня! ', day)

    def pictures_in_range_date(self, start_range_date, last_range_date):
        print('\tДелаем картинки')
        list_date = DatabaseUpdater(start_range_date=start_range_date, last_range_date=last_range_date,
                                    matrix_weather=self.matrix_weather).run()
        for day in list_date:
            day = datetime.datetime.strptime(day, '%d.%m.%Y').date()
            day = str(day.day) + '.' + str(day.month) + '.' + str(day.year)
            self.ImageMaker(day=day, matrix_weather=self.matrix_weather).run()
        print("Все даты которые были в базе сохранены в картинках!")

    def schow_in_range_date(self, start_range_date, last_range_date):
        DatabaseUpdater(start_range_date=start_range_date, last_range_date=last_range_date,
                        matrix_weather=self.matrix_weather).run()

    def run(self):
        while True:

            print()
            print('=' * 30)

            go = {"1": {"1 - Посмотреть всю БД": self.show_all},
                  "2": {"2 - Показать в диапазоне дат все данные": self.go_schow_in_range_date},
                  "3": {"3 - Показать картинки с погодой в диапазоне дат": self.go_pictures_in_range_date}}
            for line in go.values():
                for text in line.keys():
                    print(text)
            print("q - Выход")
            print('=' * 30)
            N = input("=")
            if N not in ('q', '3', '1', '2'):
                print("Такого варианта нет!")
                continue
            if N == 'q':
                break

            for line in go[N].values():
                line()

            '''
            if N == '1':
                self.show_all()
            elif N == '2':
                self.go_schow_in_range_date()
            elif N == "3":
                self.go_pictures_in_range_date()
            '''

    def go_schow_in_range_date(self):
        while True:
            print('Пример 2.10.2020')
            start = input("Введите с какой даты хотите смотреть = ")
            last = input("До какой = ")
            try:
                self.schow_in_range_date(start, last)
                break
            except Exception as e:
                print("Данные в другом фармате! ", e)

    def go_pictures_in_range_date(self):

        while True:
            print('Пример 2.11.2020')
            start = input("Введите с какой даты хотите смотреть = ")
            last = input("До какой = ")
            try:
                self.pictures_in_range_date(start, last)
                break

            except:
                print("Данные в другом фармате!")


if __name__ == '__main__':
    Main().run()
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
#зачёт!