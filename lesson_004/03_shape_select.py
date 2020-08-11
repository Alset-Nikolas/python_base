# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
# вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

color = [('Красный', sd.COLOR_RED),
         ('Оранжевый', sd.COLOR_ORANGE),
         ('Желтый', sd.COLOR_YELLOW),
         ('Зеленый', sd.COLOR_GREEN),
         ('Голубой', sd.COLOR_CYAN),
         ('Синий', sd.COLOR_BLUE),
         ('Фиолетовый', sd.COLOR_PURPLE),
         ]

figures = ['Треугольник', 'Квадрат', 'Пятиугольник', 'Шестиугольник']


def n_corners(number_of_sides, start_point=sd.Point(350, 250), angle=45, length=100, color=sd.COLOR_YELLOW):
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


def choose_color(color):
    print()
    print('\t----------------')
    print('\tВозможные цвета:')
    print('\t----------------')
    print()

    len_str = len('Фиолетовый  6')

    for i, color_ in enumerate(color):
        key = color_[0]
        print('\t', key, ' ' * (len_str - len(key)), i)

    while True:
        print()
        number_color = input('Введите желаемый цвет > ')
        if number_color.isdigit() and 0 <= int(number_color) <= 6:
            number_color = int(number_color)
        else:
            print('Вы ввели не корректный номер!')
            continue

        print()
        print('\t Хороший выбор!')
        print()
        break

    return number_color


def choose_figure(figures):
    print('\t-----------------')
    print('\tВозможные фигуры:')
    print('\t-----------------')

    len_str = len('Шестиугольник  3')
    for i, figure in enumerate(figures):
        print('\t', figure, ' ' * (len_str - len(figure)), i)

    while True:
        print()
        number_figure = input('Введите желаемую фигуру > ')
        if number_figure.isdigit() and 0 <= int(number_figure) <= 3:
            number_figure = int(number_figure)
        else:
            print('Вы ввели не корректный номер!')
            continue
        print()
        print('\t Хороший выбор!')
        print()
        break

    return number_figure


def draw(number_color, number_figure, color):
    n_corners(number_of_sides=number_figure + 3, start_point=sd.Point(300, 300),
              color=list(color[number_color][1]))


number_color = choose_color(color)
number_figure = choose_figure(figures)

draw(number_color, number_figure, color)

sd.pause()

# зачёт! 🚀
