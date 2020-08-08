# -*- coding: utf-8 -*-

import simple_draw as sd

import math


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
def draw_triangle(start_point=sd.Point(90, 90), angle=45, length=100):
    start_point_0 = start_point
    for angle_alfa in range(angle, 360 + angle, 120):
        side = sd.Vector(start_point=start_point, direction=angle_alfa, length=length, width=3)
        side.draw()
        start_point = side.end_point
    else:
        end_point = start_point
        point_list = [start_point_0, end_point]
        sd.lines(point_list, color=sd.COLOR_YELLOW, closed=False, width=3)


def draw_square(start_point=sd.Point(500, 90), angle=45, length=100):
    start_point_0 = start_point
    for angle_alfa in range(angle, 360 + angle, 90):
        side = sd.Vector(start_point=start_point, direction=angle_alfa, length=length, width=3)
        side.draw()
        start_point = side.end_point
    else:
        end_point = start_point
        point_list = [start_point_0, end_point]
        sd.lines(point_list, color=sd.COLOR_YELLOW, closed=False, width=3)


def draw_five_corners(start_point=sd.Point(120, 400), angle=45, length=100):
    start_point_0 = start_point
    for angle_alfa in range(angle, 360 + angle, 72):
        side = sd.Vector(start_point=start_point, direction=angle_alfa, length=length, width=3)
        side.draw()
        start_point = side.end_point
    else:
        end_point = start_point
        point_list = [start_point_0, end_point]
        sd.lines(point_list, color=sd.COLOR_YELLOW, closed=False, width=3)


def draw_six_corners(start_point=sd.Point(500, 400), angle=45, length=100):
    start_point_0 = start_point
    for angle_alfa in range(angle, 360 + angle, 60):
        side = sd.Vector(start_point=start_point, direction=angle_alfa, length=length, width=3)
        side.draw()
        start_point = side.end_point
    else:
        end_point = start_point
        point_list = [start_point_0, end_point]
        sd.lines(point_list, color=sd.COLOR_YELLOW, closed=False, width=3)


draw_triangle()
draw_square()
draw_five_corners()
draw_six_corners()


# draw_five_corners()
# Примерный алгоритм внутри функции:
#   # будем рисовать с помощью векторов, каждый следующий - из конечной точки предыдущего
#   текущая_точка = начальная точка
#   для угол_наклона из диапазона от 0 до 360 с шагом XXX
#      # XXX подбирается индивидуально для каждой фигуры
#      составляем вектор из текущая_точка заданной длины с наклоном в угол_наклона
#      рисуем вектор
#      текущая_точка = конечной точке вектора
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


def n_corners(number_of_sides, start_point=sd.Point(350, 250), angle=45, length=100):
    length = 100 * 6 / number_of_sides
    start_point_0 = start_point
    delta = round(360 / number_of_sides)
    for angle_alfa in range(angle, 360 + angle, delta):
        side = sd.Vector(start_point=start_point, direction=angle_alfa, length=length, width=3)
        side.draw()
        start_point = side.end_point
    else:
        end_point = start_point
        point_list = [start_point_0, end_point]
        sd.lines(point_list, color=sd.COLOR_YELLOW, closed=False, width=3)


n_corners(number_of_sides=18)

sd.pause()
