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

''' 
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
'''
distances = {
    'Moscow': {
        'London': Moscow_London,
        'Paris': Moscow_Paris
    },
    'London': {
        'Moscow': Moscow_London,
        'Paris': London_Paris
    },
    'Paris': {
        'London': London_Paris,
        'Moscow': Moscow_Paris
    }

}

pprint(distances)
# print(distances['Moscow']['Paris'])
# print(distances['Paris']['Moscow'])

# зачёт! 🚀
