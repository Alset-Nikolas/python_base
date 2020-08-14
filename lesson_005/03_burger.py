# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

import my_burger
print('\t----------------------------')

print('\t Рецепт двойного чизбургера')
print('\t----------------------------')
my_burger.add_buns()
my_burger.add_cutlets()
my_burger.add_cheeses()
my_burger.add_cutlets()
my_burger.add_cheeses()
my_burger.add_cukes()
my_burger.add_ketchup()
my_burger.add_onion()
my_burger.add_mustard()
my_burger.add_buns()
print('\t----------------------------')

print('\t----------------------------')

print('\t\t Рецепт бургера')
print('\t----------------------------')
my_burger.add_buns()
my_burger.add_cutlets()
my_burger.add_cheeses()
my_burger.add_buns()
my_burger.add_cutlets()
my_burger.add_cheeses()
my_burger.add_buns()
my_burger.add_cukes()
my_burger.add_cheeses()
my_burger.add_ketchup()
my_burger.add_onion()
my_burger.add_mustard()
my_burger.add_buns()
print('\t----------------------------')

# зачёт! 🚀
