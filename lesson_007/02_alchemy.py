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

    # , Николай, всё правильно. Но предлагаю создать дополнительный метод для классов init.
    #  Указать в нём название элемента и в __str__ выводить название элемента из __init__.
    def __init__(self):
        self.name = 'Стекло'

    def __str__(self):
        return self.name


class Sand:

    def __init__(self):
        self.name = 'Песок'

    def __str__(self):
        return self.name


class Water:

    def __init__(self):
        self.name = 'Вода'

    def __str__(self):
        return self.name


class Mud:

    def __init__(self):
        self.name = 'Грязь'

    def __str__(self):
        return self.name


class Lightning:

    def __init__(self):
        self.name = 'Молния'

    def __str__(self):
        return self.name


class Dust:

    def __init__(self):
        self.name = 'Пыль'

    def __str__(self):
        return self.name


class Lava:

    def __init__(self):
        self.name = 'Лава'

    def __str__(self):
        return self.name


class Storm:

    def __init__(self):
        self.name = 'Шторм'

    def __str__(self):
        return self.name


class Steam:

    def __init__(self):
        self.name = 'Пар'

    def __str__(self):
        return self.name


class Earth:
    def __init__(self):
        self.name = 'Земля'

    def __str__(self):
        return self.name

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
    def __init__(self):
        self.name = 'Воздух'

    def __str__(self):
        return self.name

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
    def __init__(self):
        self.name = 'Огонь'

    def __str__(self):
        return self.name

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

# зачёт!
