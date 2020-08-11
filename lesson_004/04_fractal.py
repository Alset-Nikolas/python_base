# -*- coding: utf-8 -*-
import simple_draw as sd

sd.resolution = (1200, 800)
# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,
'''
def draw_branches(point_start, angle, length):
    angle_alfa = 30
    branches = sd.Vector(start_point=point_start, direction = angle, length=length)
    left_branches = sd.Vector(start_point=branches.end_point, direction = angle+angle_alfa, length=length*0.75)
    right_branches = sd.Vector(start_point=branches.end_point, direction = angle-angle_alfa, length=length*0.75)
    branches.draw(width=3)
    left_branches.draw(width=3)
    right_branches.draw(width=3)

start = sd.Point(300,50)

draw_branches(start, 90, 100)'''

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длина ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения
'''
start = sd.Point(300,50)
def draw_branches(point_start, angle, length):
    if length < 10:
        return
    angle_alfa = 30
    branches = sd.Vector(start_point=point_start, direction = angle, length=length)
    draw_branches(point_start=branches.end_point, angle=angle+angle_alfa, length=length*0.75)
    draw_branches(point_start=branches.end_point, angle=angle-angle_alfa, length=length*0.75)
    branches.draw(width=3)
draw_branches(start, 90, 100)'''
# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()
start = sd.Point(600, 50)


def draw_branches(point_start, angle, length):
    if length < 10:
        return
    angle_alfa = sd.random_number(0.6 * 30, 1.4 * 30)
    sigma = sd.random_number(8, 12) / 10
    branches = sd.Vector(start_point=point_start, direction=angle, length=length)
    draw_branches(point_start=branches.end_point, angle=angle + angle_alfa, length=length * 0.75 * sigma)
    draw_branches(point_start=branches.end_point, angle=angle - angle_alfa, length=length * 0.75 * sigma)
    branches.draw(width=3)


draw_branches(start, 90, 150)
sd.pause()

# зачёт! 🚀
