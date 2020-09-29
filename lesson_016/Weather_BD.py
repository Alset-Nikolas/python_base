
import peewee


class Weather_BD(peewee.Model):
    date = peewee.DateField()
    weather = peewee.CharField()
    temperature = peewee.CharField()

    class Meta:
        database = peewee.SqliteDatabase("DateBase.db")

