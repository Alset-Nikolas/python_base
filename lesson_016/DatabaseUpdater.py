import os
import datetime
from pprint import pprint

import peewee

from Weather_BD import Weather_BD
from WeatherMaker import WeatherMaker


class DatabaseUpdater:
    def __init__(self, start_range_date='01.01.0001', matrix_weather={}, last_range_date="01.01.9999"):
        self.start_range_date = datetime.datetime.strptime(start_range_date, '%d.%m.%Y').date()
        self.last_range_date = datetime.datetime.strptime(last_range_date, '%d.%m.%Y').date()
        self.database = peewee.SqliteDatabase("DateBase.db")

        self.start_date_bd = None
        self.matrix_weather = matrix_weather

    def abdate_results_for_the_next_week(self):
        if not os.path.exists("DateBase.db"):
            self.database.create_tables([Weather_BD])

            for day, line in self.matrix_weather.items():
                day = datetime.datetime.strptime(day, '%d.%m.%Y')
                artist = Weather_BD.create(date=day, weather=line["погода"], temperature=line["температура"])
                artist.save()
        else:

            for day, line in self.matrix_weather.items():

                weather, created = Weather_BD.get_or_create(
                    date=day,
                    weather=line["погода"],
                    temperature=line["температура"])

                if not created:
                    query = Weather_BD.update(date=day,
                                            weather=line["погода"],
                                            temperature=line["температура"]).where(Weather_BD.id == weather.id)
                    query.execute()

        self.database.close()
        self.start_date_bd = Weather_BD.get(Weather_BD.id == 1).date

    def show_BD(self):
        for weather in Weather_BD.select():
            print(f'{weather.date} \tПогода: {weather.weather} Температура: {weather.temperature}')

    def date_range(self):
        list_date = []
        if self.start_range_date < self.start_date_bd:
            self.start_range_date = self.start_date_bd
        if self.start_range_date > self.last_range_date:
            self.start_range_date, self.last_range_date = self.last_range_date, self.start_range_date
        if self.last_range_date > datetime.datetime.now().date() + datetime.timedelta(days=9):
            self.last_range_date = datetime.datetime.now().date() + datetime.timedelta(days=9)

        query = (Weather_BD
                 .select()
                 .where(Weather_BD.date.between(self.start_range_date, self.last_range_date)))
        for weather in query:
            list_date.append(str(weather.date.strftime("%d.%m.%Y")))
            print(f'{weather.date.strftime("%d.%m.%Y")} \tПогода: {weather.weather} Температура: {weather.temperature}')
        return list_date

    def run(self):
        self.abdate_results_for_the_next_week()
        return self.date_range()


    def add_new_day(self, day, weather, temperature):
        weather, created = Weather_BD.get_or_create(
            date=day,
            weather=weather,
            temperature=temperature)

        if not created:
            query = Weather_BD.update(date=day,
                                      weather=weather,
                                      temperature=temperature).where(Weather_BD.id == weather.id)
            query.execute()

if __name__ == "__main__":
    matrix_weather = WeatherMaker().run()
    A = DatabaseUpdater(start_range_date='29.09.2020', last_range_date='3.10.2020', matrix_weather=matrix_weather).run()