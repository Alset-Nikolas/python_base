#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

# посадите медведя (bear) между львом и кенгуру
# и выведите список на консоль


zoo.insert(1, 'bear')
print(zoo)
# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark']
# и выведите список на консоль
zoo.append(birds)
print(zoo)

# уберите слона
zoo.remove('elephant')
# и выведите список на консоль
print(zoo)


# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
print('Лев сидит в клетке №', zoo.index('lion')+1, '!')
print('Жаворонок сидит в клетке №',zoo.index(birds)+1, ', а точнее в клетке №', birds.index('lark')+1, 'для птиц!')