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
import math
import os
from pprint import pprint

import requests
from bs4 import BeautifulSoup

# сегодня
from translate import Translator

class WeatherMaker:

    def __init__(self):
        self.html_text = requests.get('https://www.meteoservice.ru/weather/now/moskva', ).text
        self.soup_today = BeautifulSoup(self.html_text, 'html.parser')

        self.html_text_10days = requests.get('https://www.meteoservice.ru/weather/10days/moskva').text
        self.soup_10days = BeautifulSoup(self.html_text_10days, 'html.parser')

        self.matrix_weather = []

    def run(self):
        self._today_forecast()
        self._days10_forecast()
        return self.matrix_weather
    def _today_forecast(self):
        date = self.soup_today.find(id='point-time').contents[0]
        temperature = self.soup_today.find('span', class_='value').contents[0]
        weather = self.soup_today.find('p', class_='margin-bottom-0').contents[0]

        self.matrix_weather.append({"погода": weather, "температура": temperature, "дата":date})

    def _days10_forecast(self):
        dates = self.soup_10days.find_all(class_="text-nowrap grey font-condensed font-smaller")
        temperatures_ = self.soup_10days.find_all('div', class_="font-larger")
        weathers = self.soup_10days.find_all('div', class_="column value show-for-large text-left font-smaller")

        for i in range(1, 10):
            date = dates[i].contents[0]
            temperature = temperatures_[i].contents[0].split()[0]
            weather = weathers[i].contents[0]

            self.matrix_weather.append({"погода": weather, "температура": temperature, "дата": date})



import cv2
class ImageMaker:
    #rgb
    COLOR_WHITE = (255, 255, 255)
    COLOR_BLACK = (0, 0, 0)

    COLOR_YELLOW = (255, 255, 0)
    COLOR_BLUE = (0, 0, 255)
    COLOR_DARK_BLUE = (0, 0, 127)
    COLOR_GRAY = (127, 127, 127)

    def __init__(self):
        self.path_card_main = os.getcwd() + os.path.normpath("\\python_snippets\\external_data\\probe.jpg")

        self.path_card_cloud = os.getcwd() + os.path.normpath("\\python_snippets\\external_data\\weather_img\\cloud.jpg")
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

    def run(self):
        self.create_main_card()


        matrix_weather = WeatherMaker().run()
        pprint(matrix_weather)
        self.fone(matrix_weather)

    def fone(self, matrix_weather):
        now = matrix_weather[0]

        if now['погода'] in ['Ясно', 'Солнечно', 'Ясная погода', 'Малооблачно']:
            self.weather_picture(self.path_card_sun)
            self.color_yellow()
            self.gluing()
            self.add_text(now)
            self.schow_card(self.main_card, "main")
        elif now['погода'] in ['Дождь']:
            self.weather_picture(self.path_card_rain)
            self.color_dark_blue()
            self.gluing()
            self.schow_card(self.main_card, "main")
        elif now['погода'] in ['Снег']:
            self.weather_picture(self.path_card_snow)
            self.color_blue()
            self.gluing()
            self.schow_card(self.main_card, "main")
        elif now['погода'] in ['Облачно']:
            self.weather_picture(self.path_card_cloud)
            self.color_grey()
            self.gluing()
            self.schow_card(self.main_card, "main")
        else:
            print("Необходимо добавить такой тип погоды :", now['погода'])
            self.weather_picture(self.path_card_sun)
            self.color_yellow()
            self.gluing()
            self.schow_card(self.main_card, "main")


    def add_text(self, info):

        date = self.translate_(str(info["дата"]))
        weather = self.translate_(info["погода"])
        temper = self.translate_(info["температура"])
        Y = self.height_main_card // 2
        (x_down_left, y_down_left) = (self.width_main_card//3, Y)
        size_text = 1
        color = (111, 111, 190)
        size_letters = 3

        cv2.putText(self.main_card, date, (x_down_left, y_down_left), cv2.FONT_HERSHEY_SIMPLEX, size_text, color, size_letters)
        cv2.putText(self.main_card, weather, (self.width_main_card//3, Y + 30), cv2.FONT_HERSHEY_SIMPLEX, size_text, color,
                    size_letters)
        cv2.putText(self.main_card, temper, (self.width_main_card//3, Y + 60), cv2.FONT_HERSHEY_SIMPLEX, size_text, color,
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
                self.main_card[y, x+dx] = self.weather_card[y, x]

    def color_blue(self):
        dx_const = math.ceil((self.width_main_card / 255))

        for y in range(self.height_main_card):
            for x in range(self.width_main_card):
                if 255-int(x//dx_const) < 0 :
                    self.main_card[y, x] = [255, 255, 0]
                else:
                    self.main_card[y, x] = [255, 255, 255-int(x//dx_const)]

    def color_yellow(self):
        dx_const = math.ceil((self.width_main_card / 255))

        for y in range(self.height_main_card):
            for x in range(self.width_main_card):
                if 255-int(x//dx_const) < 0 :
                    self.main_card[y, x] = [0, 255, 255]
                else:
                    self.main_card[y, x] = [255-int(x//dx_const), 255, 255]


    def color_dark_blue(self):
        dx_const = math.ceil((self.width_main_card / 255))

        for y in range(self.height_main_card):
            for x in range(self.width_main_card):
                if 255-int(x//dx_const) < 0 :
                    self.main_card[y, x] = [255, 0, 0]
                else:
                    self.main_card[y, x] = [255, 255-int(x//dx_const), 255-int(x//dx_const)]

    def color_grey(self):
        dx_const = math.ceil((self.width_main_card / 127))

        for y in range(self.height_main_card):
            for x in range(self.width_main_card):
                if 255-int(x//dx_const) < 0 :
                    self.main_card[y, x] = [127, 127, 127]
                else:
                    self.main_card[y, x] = [255-int(x//dx_const), 255-int(x//dx_const), 255-int(x//dx_const)]

    def translate_(self, str):
        translator = Translator(from_lang='Russian',to_lang='English')
        return translator.translate(str)
    def schow_card(self, image, name_of_window):
        cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
        cv2.imshow(name_of_window, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

A = ImageMaker()
A.run()
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

# Добавить класс DatabaseUpdater с методами:
#   Получающим данные из базы данных за указанный диапазон дат.
#   Сохраняющим прогнозы в базу данных (использовать peewee)

# Сделать программу с консольным интерфейсом, постаравшись все выполняемые действия вынести в отдельные функции.
# Среди действий, доступных пользователю, должны быть:
#   Добавление прогнозов за диапазон дат в базу данных
#   Получение прогнозов за диапазон дат из базы
#   Создание открыток из полученных прогнозов
#   Выведение полученных прогнозов на консоль
# При старте консольная утилита должна загружать прогнозы за прошедшую неделю.

# Рекомендации:
# Можно создать отдельный модуль для инициализирования базы данных.
# Как далее использовать эту базу данных в движке:
# Передавать DatabaseUpdater url-путь
# https://peewee.readthedocs.io/en/latest/peewee/playhouse.html#db-url
# Приконнектится по полученному url-пути к базе данных
# Инициализировать её через DatabaseProxy()
# https://peewee.readthedocs.io/en/latest/peewee/database.html#dynamically-defining-a-database
