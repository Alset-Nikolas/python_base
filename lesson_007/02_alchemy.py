# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм+
#   Вода + Огонь = Пар+
#   Вода + Земля = Грязь+
#   Воздух + Огонь = Молния+
#   Воздух + Земля = Пыль+
#   Огонь + Земля = Лава+

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Glass:

    # TODO, Николай, всё правильно. Но предлагаю создать дополнительный метод для классов init.
    #  Указать в нём название элемента и в __str__ выводить название элемента из __init__.
    def __str__(self):
        return 'Стекло'


class Sand:
    def __str__(self):
        return 'Песок'


class Water:
    def __str__(self):
        return 'Вода'


class Mud:
    def __str__(self):
        return 'Грязь'


class Lightning:
    def __str__(self):
        return 'Молния'


class Dust:
    def __str__(self):
        return 'Пыль'


class Lava:
    def __str__(self):
        return 'Лава'


class Storm:
    def __str__(self):
        return 'Шторм'


class Steam:
    def __str__(self):
        return 'Пар'


class Earth:

    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        '''Вода + Земля = Грязь'''
        if type(other) == Water:
            return Mud()
        return None

    def __radd__(self, other):
        if type(other) == Water:
            return Mud()
        return None


class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        ''' Воздух + Огонь = Молния
            Воздух + Земля = Пыль'''
        if type(other) == Water:
            return Storm()
        elif type(other) == Fire:
            return Lightning()
        elif type(other) == Earth:
            return Dust()
        return None

    def __radd__(self, other):
        '''Вода + Воздух = Шторм'''
        if type(other) == Water:
            return Storm()
        elif type(other) == Fire:
            return Lightning()
        elif type(other) == Earth:
            return Dust()
        return None


class Fire:

    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        '''Огонь + Земля = Лава'''
        if type(other) == Water:
            return Steam()
        if type(other) == Earth:
            return Lava()
        if type(other) == Sand:
            return Glass()
        return None

    def __radd__(self, other):
        '''Вода + Огонь = Пар'''
        if type(other) == Water:
            return Steam()
        if type(other) == Earth:
            return Lava()
        if type(other) == Sand:
            return Glass()
        return None


#   Вода + Воздух = Шторм+
#   Вода + Огонь = Пар+
#   Вода + Земля = Грязь+
#   Воздух + Огонь = Молния+
#   Воздух + Земля = Пыль+
#   Огонь + Земля = Лава+

#
print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Water(), '+', Earth(), '=', Water() + Earth())
print(Air(), '+', Fire(), '=', Air() + Fire())
print(Air(), '+', Earth(), '=', Air() + Earth())
print(Fire(), '+', Earth(), '=', Fire() + Earth())
print(Fire(), '+', Sand(), '=', Fire() + Sand())

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
