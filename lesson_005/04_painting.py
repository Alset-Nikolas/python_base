# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги+
#  - стены+
#  - дерева+
#  - смайлика+
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик. +
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)
import simple_draw as sd
from drawing_old_pictures.house import hose_draw
from animation_painting.snowfall import snowfall_draw
from drawing_old_pictures.rainbow import rainbow_picture
from drawing_old_pictures.street import street_draw
from drawing_old_pictures.tree import tree_draw
from animation_painting.sun import sun_draw
from animation_painting.smile import smile_draw




# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.


X_SIZE = 1200
Y_SIZE = 800

sd.resolution = (X_SIZE, Y_SIZE)

snowfall_x, snowfall_y, snowfall_length, flag_add_new_snowfall, N = [], [], [], [], 20

first_color = 0
delta_for_sun = 0
x_start_for_kolobok = 20

hose_draw(x_left_down=X_SIZE // 2 - 200, y_left_down=200, x_size=400, y_size=300)
tree_draw(x_start=X_SIZE // 2 + 400, y_start=200, length=100)

while True:

    rainbow_picture(x_center=420, y_center=150, radius=800, first_color=first_color)
    first_color = (first_color + 1) % 7


    snowfall_x, snowfall_y, snowfall_length, flag_add_new_snowfall, N = \
        snowfall_draw(x_coordinates_down=0,
                      y_coordinates_down=200,
                      x_coordinates_up=X_SIZE // 2 - 200 - 50,
                      y_coordinates_up=Y_SIZE - 200,
                      start_x=snowfall_x,
                      start_y=snowfall_y,
                      snowfall_length=snowfall_length,
                      flag_add_new_snowfall=flag_add_new_snowfall,
                      N=N)

    delta_for_sun = sun_draw(100, Y_SIZE - 60, 30, delta_for_sun)

    street_draw(X_SIZE, 200)
    smile_draw(x_strart=x_start_for_kolobok, y_start=150)
    x_start_for_kolobok += 5

    print(locals())
    sd.sleep(0.3)
    if sd.user_want_exit():
        break
