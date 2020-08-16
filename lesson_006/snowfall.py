# -*- coding: utf-8 -*-
# сделать модуль snowfall.py в котором реализовать следующие функции

#  создать_снежинки(N) - создает N снежинок +
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color+
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг+
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана+
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка+
# снежинки хранить в глобальных переменных модуля snowfall

import simple_draw as sd

sd.resolution = (800, 800)
start_x = []
start_y = []
snowfall_length = []
quantity_snowfall = 0


def create_snowfall(N):
    global snowfall_length, quantity_snowfall
    global start_x, start_y
    quantity_snowfall += N
    for _ in range(N):
        start_x += [sd.random_number(0, 800)]
        start_y += [sd.random_number(0, 800)]
        snowfall_length += [sd.random_number(5, 10)]


def draw_snowfall(color):
    global SNOWFALL
    start_point = [sd.Point(start_x[i], start_y[i]) for i in range(quantity_snowfall)]
    SNOWFALL = [sd.snowflake(center=start_point[i],
                             length=snowfall_length[i], color=color) for i in range(quantity_snowfall)]


def dy_snowfall():
    global start_x, start_y
    for i in range(quantity_snowfall):
        start_y[i] -= 5
        start_x[i] += sd.randint(-3, 3)


def exit_border_snowfall():
    res = []
    for i, y in enumerate(start_y):
        if y - snowfall_length[i] <= 0:
            res.append(i)
    return sorted(res, reverse=True)


def del_snowfall(res):
    global quantity_snowfall
    global start_x, start_y
    draw_snowfall(color=sd.background_color)

    for i in res:
        start_x.pop(i)
        start_y.pop(i)
        snowfall_length.pop(i)

    quantity_snowfall -= len(res)
    draw_snowfall(color=sd.COLOR_WHITE)
