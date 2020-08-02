#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pprint import pprint

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

Moscow = sites["Moscow"]
London = sites["London"]
Paris = sites["Paris"]

Moscow_London = ((Moscow[0] - London[0]) ** 2 + (Moscow[1] - London[1]) ** 2) ** 0.5
Moscow_Paris = ((Moscow[0] - Paris[0]) ** 2 + (Moscow[1] - Paris[1]) ** 2) ** 0.5
London_Paris = ((London[0] - Paris[0]) ** 2 + (London[1] - Paris[1]) ** 2) ** 0.5

distances = {}
distances['Moscow'] = {}
distances['Moscow']['London'] = Moscow_London
distances['Moscow']['Paris'] = Moscow_Paris

distances['London'] = {}
distances['London']['Moscow'] = Moscow_London
distances['London']['Paris'] = London_Paris

distances['Paris'] = {}
distances['Paris']['Moscow'] = Moscow_Paris
distances['Paris']['London'] = London_Paris

pprint(distances)

# TODO в целом у Вас очень хороший вариант решения! Попробуйте улучшить код: создайте словарь distances "одним махом".
#  Вы создали 3 пустых словаря внутри distances, а затем начали по 1ому добавлять в него ключи. Сделайте так:
#       1. так же используйте готовые переменные (moscow_paris, london_paris, moscow_london);
#       2. создайте словарь distances "одним махом". Т.е. при создании мы заодно инициализируем словарь.
#          Пример инициализации словаря при создании:
#           color_yellow = 'желтый'
#           color_red = 'Красная'
#           fairytale_heroes = {
#              'Колобок': {
#                  'Колобок': color_yellow,
#                  'Дед': 'старый',
#                  'Бабка': 'молодая',
#              },
#              'Красная Шапочка': {
#                  'Шапочка': color_red
#              }
#          }
#      .
#      В примере мы создаем словарь fairytale_heroes, который имеет 2 Вложенных словаря: по ключу 'Колобок' и
#      по ключу 'Красная Шапочка'. Аналогично можно проинициализировать и distances:
#        distances = {
#           ...
#        }
#      Это сделает код компактнее и удобнее для понимания. Одного взгляда будет достаточно, чтобы понять, что хранится
#      в словаре и какую структуру он имеет. Особенно удобно, когда словарь имеет большой размер или используется в
#      качестве конфигурации чего-либо.
#      .
#     В итоге для получения расстояния, например, между Москвой и Парижем, можно использовать оба выражения:
#          distances['Moscow']['Paris']
#          distances['Paris']['Moscow']        # оба доступны
