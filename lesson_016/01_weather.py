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


class WeatherMaker:

    def __init__(self):
        self.html_text = requests.get('https://www.meteoservice.ru/weather/now/moskva', ).text
        self.soup_today = BeautifulSoup(self.html_text, 'html.parser')

        self.html_text_10days = requests.get('https://www.meteoservice.ru/weather/10days/moskva').text
        self.soup_10days = BeautifulSoup(self.html_text_10days, 'html.parser')

        self.matrix_weather = {}

    def run(self):
        self._days10_forecast()
        return self.matrix_weather

    def _days10_forecast(self):
        dates = self.soup_10days.find_all(class_="text-nowrap grey font-condensed font-smaller")
        temperatures_ = self.soup_10days.find_all('div', class_="font-larger")
        weathers = self.soup_10days.find_all('div', class_="column value show-for-large text-left font-smaller")

        MONTHS = {"января": '01',
                  "февраля": '02',
                  "марта": '03',
                  "апреля": '04',
                  "мая": '05',
                  "июня": '06',
                  "июля": '07',
                  "августа": '08',
                  "сентября": '09',
                  "октября": '10',
                  "ноября": '11',
                  "декабря": '12',
                  }

        for i in range(0, 10):
            date = dates[i].contents[0]
            date = date.split()
            date = date[0] + '.' + MONTHS[date[1]] + '.' + str(datetime.datetime.now().year)

            temperature = temperatures_[i].contents[0].split()[0]
            weather = weathers[i].contents[0]

            self.matrix_weather[date] = {"погода": weather, "температура": temperature}


class ImageMaker:
    COLOR_WHITE = [255, 255, 255]
    COLOR_BLACK = [0, 0, 0]

    def __init__(self, day):
        self.path_card_main = os.getcwd() + os.path.normpath("\\python_snippets\\external_data\\probe.jpg")

        self.path_card_cloud = os.getcwd() + os.path.normpath(
            "\\python_snippets\\external_data\\weather_img\\cloud.jpg")
        self.path_card_rain = os.getcwd() + os.path.normpath("\\python_snippets\\external_data\\weather_img\\rain.jpg")
        self.path_card_snow = os.getcwd() + os.path.normpath("\\python_snippets\\external_data\\weather_img\\snow.jpg")
        self.path_card_sun = os.getcwd() + os.path.normpath("\\python_snippets\\external_data\\weather_img\\sun.jpg")

        self.main_card = None
        self.height_main_card = None
        self.width_main_card = None
        self.size_main_card = None

        self.weather_card = None
        self.width_weather_card = None
        self.height_weather_card = None
        self.size_weather_card = None

        self.matrix_weather = None

        self.day = day

    def run(self):
        self.create_main_card()
        self.matrix_weather = WeatherMaker().run()
        self.creating_card_for_specific_day(self.day)

    def creating_card_for_specific_day(self, day):

        if self.matrix_weather[day]["погода"] in ['Ясно', 'Солнечно', 'Ясная погода', 'Малооблачно']:
            self.weather_picture(self.path_card_sun)
            self.color_yellow()
            self.gluing()
            self.add_text(day)
            self.schow_card(self.main_card, "main")
        elif self.matrix_weather[day]["погода"] in ['Дождь']:
            self.weather_picture(self.path_card_rain)
            self.color_dark_blue()
            self.gluing()
            self.add_text(day)
            self.schow_card(self.main_card, "main")
        elif self.matrix_weather[day]["погода"] in ['Снег']:
            self.weather_picture(self.path_card_snow)
            self.color_blue()
            self.gluing()
            self.add_text(day)
            self.schow_card(self.main_card, "main")
        elif self.matrix_weather[day]["погода"] in ['Облачно', "Пасмурно"]:
            self.weather_picture(self.path_card_cloud)
            self.color_grey()
            self.gluing()
            self.add_text(day)
            self.schow_card(self.main_card, "main")
        else:
            print("Необходимо добавить такой тип погоды :", self.matrix_weather[day]["погода"])
            self.weather_picture(self.path_card_sun)
            self.color_yellow()
            self.gluing()
            self.add_text(day)
            self.schow_card(self.main_card, "main")

    def add_text(self, day):

        date = day
        weather = self.matrix_weather[day]["погода"]
        temper = self.matrix_weather[day]["температура"].replace('…', '...')[:-1]
        Y = self.height_main_card // 2
        (x_down_left, y_down_left) = (self.width_main_card // 3, Y)
        size_text = 1
        color = (111, 111, 190)
        size_letters = 3

        cv2.putText(self.main_card, date, (x_down_left, y_down_left), cv2.FONT_HERSHEY_COMPLEX, size_text, color,
                    size_letters)
        cv2.putText(self.main_card, weather, (self.width_main_card // 3, Y + 30), cv2.FONT_HERSHEY_COMPLEX, size_text,
                    color,
                    size_letters)
        cv2.putText(self.main_card, temper, (self.width_main_card // 3, Y + 60), cv2.FONT_HERSHEY_COMPLEX, size_text,
                    color,
                    size_letters)

    def create_main_card(self):
        self.main_card = cv2.imread(self.path_card_main)
        self.width_main_card = 800
        self.height_main_card = 400
        self.size_main_card = (self.width_main_card, self.height_main_card)
        self.main_card = cv2.resize(self.main_card, self.size_main_card, interpolation=cv2.INTER_AREA)

    def weather_picture(self, path_picture):
        self.weather_card = cv2.imread(path_picture)
        self.width_weather_card = self.weather_card.shape[1]
        self.height_weather_card = self.weather_card.shape[0]
        self.size_weather_card = (self.width_weather_card, self.height_weather_card)
        self.weather_card = cv2.resize(self.weather_card, self.size_weather_card, interpolation=cv2.INTER_AREA)

    def gluing(self):
        dx = self.width_main_card - self.width_weather_card
        dy = self.height_main_card - self.height_weather_card
        for x in range(self.width_weather_card):
            for y in range(self.height_weather_card):
                self.main_card[y, x + dx] = self.weather_card[y, x]

    def color_blue(self):
        COLOR_BLUE = [255, 255, 0]

        dx_const = math.ceil((self.width_main_card / 255))

        for y in range(self.height_main_card):
            for x in range(self.width_main_card):
                if 255 - int(x // dx_const) < 0:
                    self.main_card[y, x] = COLOR_BLUE
                else:
                    self.main_card[y, x] = [255, 255, 255 - int(x // dx_const)]

    def color_yellow(self):
        COLOR_YELLOW = [0, 255, 255]

        dx_const = math.ceil((self.width_main_card / 255))

        for y in range(self.height_main_card):
            for x in range(self.width_main_card):
                if 255 - int(x // dx_const) < 0:
                    self.main_card[y, x] = COLOR_YELLOW
                else:
                    self.main_card[y, x] = [255 - int(x // dx_const), 255, 255]

    def color_dark_blue(self):
        COLOR_DARK_BLUE = [255, 0, 0]

        dx_const = math.ceil((self.width_main_card / 255))

        for y in range(self.height_main_card):
            for x in range(self.width_main_card):
                if 255 - int(x // dx_const) < 0:
                    self.main_card[y, x] = COLOR_DARK_BLUE
                else:
                    self.main_card[y, x] = [255, 255 - int(x // dx_const), 255 - int(x // dx_const)]

    def color_grey(self):
        COLOR_GRAY = [127, 127, 127]
        dx_const = math.ceil((self.width_main_card / 127))

        for y in range(self.height_main_card):
            for x in range(self.width_main_card):
                if 255 - int(x // dx_const) < 0:
                    self.main_card[y, x] = COLOR_GRAY
                else:
                    self.main_card[y, x] = [255 - int(x // dx_const), 255 - int(x // dx_const),
                                            255 - int(x // dx_const)]

    def translate_(self, str):
        str = str.lower()
        translator = Translator(from_lang='Russian', to_lang='English')
        str = str.split()
        otvet = ''
        for slovo in str:
            otvet += translator.translate(slovo) + ' '

        return otvet.capitalize()

    def schow_card(self, image, name_of_window):
        cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
        cv2.imshow(name_of_window, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


class Weather_BD(peewee.Model):
    date = peewee.DateTimeField()
    weather = peewee.CharField()
    temperature = peewee.CharField()

    class Meta:
        database = peewee.SqliteDatabase("DateBase.db")


class DatabaseUpdater:
    def __init__(self, start_range_date, last_range_date=datetime.datetime.now()):
        self.start_range_date = datetime.datetime.strptime(start_range_date, '%d.%m.%Y').date()
        self.last_range_date = datetime.datetime.strptime(last_range_date, '%d.%m.%Y').date()

        self.database = peewee.SqliteDatabase("DateBase.db")

        self.start_date_bd = None
        self.matrix_weather = WeatherMaker().run()

    def abdate_results_for_the_next_week(self):
        if not os.path.exists("DateBase.db"):
            self.database.create_tables([Weather_BD])

            for day, line in self.matrix_weather.items():
                artist = Weather_BD.create(date=day, weather=line["погода"], temperature=line["температура"])
                artist.save()
        else:

            for day, line in self.matrix_weather.items():
                try:
                    probe = Weather_BD.get(Weather_BD.date == day)
                    probe.weather = line['погода']
                    probe.temperature = line["температура"]
                    probe.save()
                    print('Обновил ', day)
                except:
                    new_day = Weather_BD.create(date=day, weather=line["погода"], temperature=line["температура"])
                    new_day.save()
                    print('Добавил ', new_day)
        self.database.close()
        self.start_date_bd = datetime.datetime.strptime(Weather_BD.get(Weather_BD.id == 1).date, '%d.%m.%Y').date()

    def show_BD(self):
        for weather in Weather_BD.select():
            print(f'{weather.date} \tПогода: {weather.weather} Температура: {weather.temperature}')

    def date_range(self):

        if self.start_range_date < self.start_date_bd:
            self.start_range_date = self.start_date_bd
        if self.start_range_date > self.last_range_date:
            self.start_range_date, self.last_range_date = self.last_range_date, self.start_range_date
        if self.last_range_date > datetime.datetime.now().date() + datetime.timedelta(days=9):
            self.last_range_date = datetime.datetime.now().date() + datetime.timedelta(days=9)
        print()
        for weather in Weather_BD.select():
            if self.start_range_date <= datetime.datetime.strptime(weather.date,
                                                                   '%d.%m.%Y').date() <= self.last_range_date:
                print(f'{weather.date} \tПогода: {weather.weather} Температура: {weather.temperature}')

    def run(self):
        self.abdate_results_for_the_next_week()
        self.date_range()


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


class Main:
    def __init__(self):
        pass

    def create_bd(self):
        if not os.path.exists("DateBase.db"):
            print("Создали БД! Теперь есть прогнозы на 10 дней")
            WeatherMaker().run()
        else:
            print("БД уже есть!")

    def add_new_day(self, day, weather, temperature):
        print("\tДобавим новый день!")
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
        for weather in Weather_BD.select():
            if start_range_date <= datetime.datetime.strptime(weather.date, '%d.%m.%Y').date() <= last_range_date:
                ImageMaker(day=weather.date).run()

    def schow_in_range_date(self, start_range_date, last_range_date):
        DatabaseUpdater(start_range_date=start_range_date, last_range_date=last_range_date).run()


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
        exit()
    elif N == '1':
        A.create_bd()
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
