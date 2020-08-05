# -*- coding: utf-8 -*-
import random

import simple_draw as sd


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

sd.resolution = (1200, 600)
'''
point = sd.Point(x=300, y=300)
radius = 50
for _ in range(3):
    sd.circle(center_position=point, radius=radius, width=2)
    radius += 5
'''
# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет

def draw_bubble(point, step, color):
    radius = 50
    for _ in range(3):
        sd.circle(center_position=point, radius=radius, width=2, color=color)
        radius += step



# Нарисовать 10 пузырьков в ряд


for x in range(100, 1100, 100):
    point = sd.Point(x=x, y=100)
    bubbles(point=point, step=5)  # TODO эту часть задания нужно тоже доработать по принципу остальных уже исправленных



# Нарисовать три ряда по 10 пузырьков
for y in range(100, 400, 100):
    for x in range(100, 1100, 100):
        point = sd.Point(x=x, y=y)
        draw_bubble(point=point, step=5, color=sd.COLOR_ORANGE)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    step = random.randint(2, 10)
    draw_bubble(point=point, step=step, color=sd.random_color())

sd.pause()
