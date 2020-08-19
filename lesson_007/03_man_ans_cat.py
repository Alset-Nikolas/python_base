# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).+
# Кот живет с человеком в доме.+
# Для кота дом характеризируется - миской для еды и грязью.+
# Изначально в доме нет еды для кота и нет грязи.+

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.+
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.+
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.+
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)+

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.+
# Когда кот спит - сытость уменьшается на 10+
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.+
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5+
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение+
# что будет делать сегодня+

# Человеку и коту надо вместе прожить 365 дней.


from random import randint
from termcolor import cprint

class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.cat = None


    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness,
        )

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='magenta')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='magenta')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='magenta')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='red')

    def pick_up_cat(self, cat):
        self.cat = cat
        cprint('{} взял кота {}!'.format(self.name, self.cat.name), color='red')

    def buy_cat_food(self):
        '''кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.'''
        if self.house.money >= 50:
            self.house.cat_food += 50
            self.house.money -= 50
            cprint('{} купил корм коту!'.format(self.name), color='magenta')
        else:
            cprint('{} хотел купить корм, но денег {}!'.format(self.name, self.house.money), color='magenta')

    def clean_the_house(self):
        '''степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.'''

        self.house.degree_of_dirt -= 100
        self.house.food -=20
        if self.house.degree_of_dirt< 0 :
            self.house.degree_of_dirt = 0
        cprint('{} убрался'.format(self.name), color='magenta')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.cat_food < 10:
            self.buy_cat_food()
        elif self.house.money < 50 or self.house.cat_food<50 or self.house.food<20:
            self.work()
        elif self.house.degree_of_dirt>30:
            self.clean_the_house()
        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.food = 50
        self.money = 50

        self.degree_of_dirt = 0
        self.cat_food = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, степень грязи {}, кол-во еды у кота {}'.format(
            self.food, self.money,self.degree_of_dirt,self.cat_food
        )



class Cat:

    def __init__(self, name=None, satiety=20, house=None):
        self.name = name
        self.satiety = satiety
        self.house = house

    def __str__(self):
        return 'Я кот {}, сытость {}'.format(self.name, self.satiety)

    def eat(self):
        if self.house.cat_food>=10:
            self.satiety +=20
            self.house.cat_food -= 10
            cprint('Кот кушает!', color='yellow')
        else:
            cprint('Кот мяучит, что хочет есть!! Но нет еды!',color='yellow')

    def sleep(self):
        self.satiety -= 10
        cprint('Кот спит!',color='yellow')


    def tear_Wallpaper(self):
        self.satiety -= 10
        self.house.degree_of_dirt +=5
        cprint('Кот грязнит!',color='yellow')

    def act(self):
        if self.satiety <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 3)
        if self.satiety <= 10:
            self.eat()
        elif dice == 1:
            self.sleep()
        elif dice == 2:
            self.eat()
        else:
            self.tear_Wallpaper()



citizen = Man(name='Бивис')
home = House()
cats = [Cat(name='Барсик', house=home), Cat(name='Дима', house=home), Cat(name='Витя', house=home)]

citizen.go_to_the_house(house=home)
for cat in cats:
    citizen.pick_up_cat(cat=cat)

print(citizen)
for cat in cats:
    print(cat)

print(home)

for day in range(1, 366):
    cprint('================ день {} =================='.format(day), color='blue')
    citizen.act()
    for cat in cats:
        cat.act()
    cprint('--- в конце дня ---', color='blue')
    print(citizen)
    print(home)
    for cat in cats:
        print(cat)
# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
