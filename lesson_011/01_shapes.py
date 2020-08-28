# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):

    def n_corners(point=sd.Point(350, 250), angle=45, length=100):
        length = 100 * 6 / n
        start_point_0 = point
        delta = round(360 / n)
        for angle_alfa in range(angle, 360 + angle, delta):
            side = sd.Vector(start_point=point, direction=angle_alfa, length=length, width=3)
            side.draw()
            point = side.end_point
        else:
            end_point = point
            point_list = [start_point_0, end_point]
            sd.lines(point_list, color=sd.COLOR_YELLOW, closed=False, width=3)
    return n_corners

draw_triangle = get_polygon(n=3)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)


sd.pause()
