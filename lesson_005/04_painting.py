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
from lesson_005.drawing_old_pictures.house import hose_draw
from lesson_005.drawing_old_pictures.snowfall import snowfall_draw
from lesson_005.drawing_old_pictures.rainbow import rainbow_picture
from lesson_005.drawing_old_pictures.street import street
from lesson_005.drawing_old_pictures.tree import tree_draw


X_SIZE = 1200
Y_SIZE = 800
sd.resolution = (X_SIZE, Y_SIZE)

hose_draw(x_left_down=X_SIZE // 2 - 200, y_left_down=200, x_size=400, y_size=300)
rainbow_picture(x_center=420, y_center=150, radius=800)
street(X_SIZE, 200)
tree_draw(x_start=X_SIZE // 2 + 400, y_start=200, length=100)
snowfall_draw(x_coordinates_down=0, y_coordinates_down=200,
             x_coordinates_up=X_SIZE // 2 - 200-50, y_coordinates_up=Y_SIZE)
sd.pause()
# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.

#TODO Усложненное задание делаю, но получается, что все снежинки и движ. предметы будут в 1 цикле?)