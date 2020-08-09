# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длин лучей снежинок (от 10 до 100) и пусть все снежинки будут разные
sd.resolution = (700, 700)
N = 20

# Пригодятся функции
# sd.get_psd.snowflake()
# # sd.sleep()oint()
#
# sd.random_number()
# sd.user_want_exit()

sd.start_drawing()
sd.finish_drawing()

start_x = [0] * N
start_y = [0] * N
snowfall_length = [0] * N
start_point = [0] * N
flag_add_new_snowfall = [0] * N
for i in range(N):
    start_x[i] = sd.random_number(100, 600)
    start_y[i] = sd.random_number(100, 600)
    snowfall_length[i] = sd.random_number(10, 30)
    start_point[i] = sd.Point(start_x[i], start_y[i])


def add_snowfall():
    start_x.append(sd.random_number(100, 600))
    start_y.append(sd.random_number(100, 600))
    snowfall_length.append(sd.random_number(10, 30))
    start_point.append(sd.Point(start_x[i], start_y[i]))
    flag_add_new_snowfall.append(0)


while True:
    sd.start_drawing()

    for i in range(N):
        sd.snowflake(center=start_point[i], length=snowfall_length[i], color=sd.background_color)
        if start_y[i] - snowfall_length[i] <= 0 and flag_add_new_snowfall[i] == 0:
            add_snowfall()
            N += 1
            flag_add_new_snowfall[i] = 1
        elif start_y[i] - snowfall_length[i] <= 0 and flag_add_new_snowfall[i] == 1:
            start_y[i] -= 0
            start_x[i] -= 0
        else:
            start_y[i] -= sd.random_number(1, 5)
            start_x[i] -= sd.random_number(-2, 2)
        start_point[i] = sd.Point(start_x[i], start_y[i])
        sd.snowflake(center=start_point[i], length=snowfall_length[i], color=sd.COLOR_WHITE)

    sd.sleep(0.1)

    if sd.user_want_exit():
        break
    sd.finish_drawing()

# Примерный алгоритм отрисовки снежинок
#   навсегда
#     очистка экрана
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       изменить координата_у и запомнить её в списке по индексу
#       создать точку отрисовки снежинки по координатам
#       нарисовать снежинку белым цветом в этой точке
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла: полная очистка всего экрана - долгая операция.
# - использовать хак для стирания старого положения снежинки:
#       отрисуем её заново на старом месте, но цветом фона (sd.background_color) и она исчезнет!
# - использовать функции sd.start_drawing() и sd.finish_drawing()
#       для начала/окончания отрисовки кадра анимации
# - между start_drawing и finish_drawing библиотека sd ничего не выводит на экран,
#       а сохраняет нарисованное в промежуточном буфере, за счет чего достигается ускорение анимации
# - в момент вызова finish_drawing все нарисованное в буфере разом покажется на экране
#
# Примерный алгоритм ускоренной отрисовки снежинок
#   навсегда
#     начать рисование кадра
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     закончить рисование кадра
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
