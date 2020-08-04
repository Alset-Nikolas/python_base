# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
x_size, y_size = 100, 50
left_bottom = sd.Point(0, 0)
right_top = sd.Point(x_size, y_size)

for i, y_new in enumerate(range(0, 700, y_size)):

    if i % 2 == 0:
        x_start = 0
    else:
        x_start = -x_size // 2

    for x_new in range(x_start, 700, x_size):
        sd.rectangle(left_bottom, right_top, color=sd.COLOR_ORANGE, width=3)

        left_bottom = sd.Point(x_new, y_new)
        right_top = sd.Point(x_size + x_new, y_size + y_new)

# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

sd.pause()
