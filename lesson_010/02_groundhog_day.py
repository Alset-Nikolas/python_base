# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
from random import randint

ENLIGHTENMENT_CARMA_LEVEL = 777


class ErrorDay(Exception):
    def __init__(self, day, message=None):
        self.message = message
        self.day = day

    def __str__(self):
        return 'День ' + str(self.day) + ', ' + self.message


class IamGodError(ErrorDay):
    pass


class DrunkError(ErrorDay):
    pass


class CarCrashError(ErrorDay):
    pass


class GluttonyError(ErrorDay):
    pass


class DepressionError(ErrorDay):
    pass


class SuicideError(ErrorDay):
    pass


def one_day():
    global day
    probability = randint(1, 13)
    if probability == 13:
        day += 1
        Errors = [IamGodError(day, 'Я БОГ'), DrunkError(day, 'Напился'), CarCrashError(day, 'Разбился'),
                  GluttonyError(day, 'Обожрался'), DepressionError(day, 'Депрессия'),
                  SuicideError(day, 'Самоубийство')]

        raise Errors[randint(0, 5)]
    day += 1
    return randint(1, 7)


carma = 0
day = 0
while carma < ENLIGHTENMENT_CARMA_LEVEL:

    try:
        carma += one_day()
    except (IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError) as arg:
        with open('groundhog.log', 'a', encoding='utf-8') as file:
            file.write(str(arg) + '\n')

else:
    with open('groundhog.log', 'a', encoding='utf-8') as file:
        file.write(f'Все! carma = {carma}')

# https://goo.gl/JnsDqu

# зачёт! 🚀
