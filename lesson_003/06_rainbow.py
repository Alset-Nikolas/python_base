# -*- coding: utf-8 -*-
import simple_draw as sd

# (цикл for)


rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)


start_x, start_y = 50, 50
finish_x, finish_y = 350, 450
for color in rainbow_colors:
    point_1 = sd.Point(start_x, start_y)
    point_2 = sd.Point(finish_x, finish_y)
    point_list = [point_1, point_2]
    sd.lines(point_list, color=color, closed=False, width=4)
    start_x += 5
    finish_x += 5

# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

radius = 550
center_position = sd.Point(600, 0)

for color in rainbow_colors[::-1]:
    sd.circle(center_position, radius=radius, color=color, width=10)
    radius += 10
sd.pause()

# зачёт! 🚀
