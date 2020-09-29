from pprint import pprint

import requests
from bs4 import BeautifulSoup
import datetime


class WeatherMaker:
    """
        Парсим сайт с погодой,
        self.matrix_weather: получаем словарь {'1.10.2020': {'погода': 'Ясная погода', 'температура': '+10…+20°'}}
    """
    def __init__(self):
        self.html_text = requests.get('https://www.meteoservice.ru/weather/now/moskva', ).text
        self.soup_today = BeautifulSoup(self.html_text, 'html.parser')

        self.html_text_10days = requests.get('https://www.meteoservice.ru/weather/10days/moskva').text
        self.soup_10days = BeautifulSoup(self.html_text_10days, 'html.parser')

        self.matrix_weather = {}

    def run(self):
        '''Создаю словарь данных'''
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


if __name__ ==  '__main__':
    weather_news = WeatherMaker().run()
    pprint(weather_news)
