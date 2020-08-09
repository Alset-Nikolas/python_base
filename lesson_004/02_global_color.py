# -*- coding: utf-8 -*-
import simple_draw as sd
from pprint import pprint


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

def n_corners(number_of_sides, start_point=sd.Point(350, 250), angle=45, length=50, color=sd.COLOR_YELLOW):
    length = length * 6 / number_of_sides
    start_point_0 = start_point
    delta = round(360 / number_of_sides)
    for angle_alfa in range(angle, 360 + angle, delta):
        side = sd.Vector(start_point=start_point, direction=angle_alfa, length=length, width=3)
        side.draw(color=color)
        start_point = side.end_point
    else:
        end_point = start_point
        point_list = [start_point_0, end_point]
        sd.lines(point_list, color=color, closed=False, width=3)


color = {
    0:
        {'Красный': sd.COLOR_RED},
    1:
        {'Оранжевый': sd.COLOR_ORANGE},
    2:
        {'Желтый': sd.COLOR_YELLOW},
    3:
        {'Зеленый': sd.COLOR_GREEN},
    4:
        {'Голубой': sd.COLOR_CYAN},
    5:
        {'Синий': sd.COLOR_BLUE},
    6:
        {'Фиолетовый': sd.COLOR_PURPLE},
}
print('Возможные цвета:')
len_str = len('Красный 	 0')

for i in color:
    key = list(color[i].keys())[0]
    print('\t', key, ' ' * (len_str - len(key)), i)


while True:
    number_color = input('Введите желаемый цвет > ')
    try:
        number_color = int(number_color)
    except:
        print('Вы ввели не корректный номер!')
    if isinstance(number_color, int) and 0 <= number_color <= 6:
        for n in range(3, 7, 1):
            #print('Я залагал тут! Должен нарисовать правильный ', n,' угольник!')
            n_corners(number_of_sides=n, start_point=sd.random_point(), color=list(color[number_color].values())[0])
    else:
        print('Вы ввели не корректный номер!')

sd.pause()

