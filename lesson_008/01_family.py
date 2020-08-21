# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,+
#   играть в WoT,+
#   ходить на работу,
# Жена может:
#   есть,+
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:+
#   кол-во денег в тумбочке (в начале - 100)+
#   кол-во еды в холодильнике (в начале - 50)+
#   кол-во грязи (в начале - 0)+
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).+
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов+
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self, money=100, food=50, dirt=0, food_cat=30):
        self.money = money
        self.food = food
        self.dirt = dirt
        self.cat_food = food_cat

    def __str__(self):
        return '{}: денег {}, еды {}, грязи {}, еды у кота {}'.format(
            self.__class__.__name__, self.money, self.food, self.dirt, self.cat_food)


class Human:

    def __init__(self, name=None, richness=30, happiness=100):
        self.name = name
        self.richness = richness
        self.happiness = happiness
        self.house = None

    def __str__(self):
        return '{}: степень сытости {}, cтепень счастья {}'.format(self.name, self.richness, self.happiness)

    def eat(self):
        if self.house.food >= 20:
            self.richness += 20
            self.house.food -= 20
            print('{} поел 20 еды!'.format(self.name))
        else:
            if self.house.food >= 10:
                piece = randint(10, self.house.food)
                self.richness += piece
                self.house.food -= piece
                print('{} поел {} еды!'.format(self.name, piece))
            else:
                piece = self.house.food // 2
                self.richness += piece
                self.house.food -= piece
                print('{} поел {} еды!'.format(self.name, piece))

    def go_to_house(self, house):
        self.house = house
        print('{} вьехал в дом!'.format(self.name))

    def cleaning_house(self):
        if self.house.dirt > 90:
            self.happiness -= 10
            print('{} живет в грязи!'.format(self.name))
        else:
            print('{} рад(а), что чисто!'.format(self.name))

    def alive(self):
        if self.richness <= 0 or self.happiness < 0:
            print('{} умер'.format(self.name))
            return True
        return False

    def pet_the_cat(self):
        self.happiness += 5
        print('{} погладил(а) кота!'.format(self.name))


class Husband(Human):
    def __init__(self, name, salary=150):
        super().__init__(name)
        self.salary = salary

    def act(self):
        monet = randint(1, 10)
        super().cleaning_house()
        if not super().alive():
            if self.richness < 20:
                self.eat()
            elif self.happiness <= 11:
                self.gaming()
            elif self.house.money <= 200:
                self.work()
            elif 0 >= monet >= 8:
                self.work()
            elif monet > 8 and self.house.money > 150:
                self.pet_the_cat()
            else:
                print('EROR!')
            return True
        else:
            return False

    def work(self):
        self.richness -= 10
        self.house.money = self.salary
        print('{} сходил на работу!'.format(self.name) if self.richness > 0
              else '{} умер на работе!'.format(self.name))

    def gaming(self):
        self.richness -= 10
        self.happiness += 20
        print('{} победил в WoT!'.format(self.name) if self.richness > 0
              else '{} умер, но победил в WoT !'.format(self.name))


class Wife(Human):

    def __init__(self, name):
        super().__init__(name=name)
        self.number_fur_coats = 0

    def act(self):
        super().cleaning_house()
        if not super().alive():
            if self.richness <= 10 and self.house.food>0:
                self.eat()
            elif self.happiness <= 10 and self.house.dirt >= 70:
                self.clean_house()
            elif self.house.food <= 30:
                self.shopping()
            elif self.house.cat_food <= 50 :
                self.buy_food_cat()
            elif 50 < self.house.dirt:
                self.clean_house()
            elif self.happiness <= 10 and self.house.cat_food > 30:
                self.pet_the_cat()
            elif self.house.food > 100 and self.house.cat_food > 100 and self.house.dirt < 30:
                self.buy_fur_coat()
            return True
        else:
            return False

    def shopping(self):
        self.richness -= 10
        if self.house.money >= 40:
            self.house.money -= 40
            self.house.food += 40
            print('{} купила 60 еды!'.format(self.name))
        else:
            if self.house.money >= 30:
                piece = randint(30, self.house.money)
                self.house.food += piece
                self.house.money -= piece
                print('{} купила {} еды!'.format(self.name, piece))
            else:
                piece = self.house.money
                self.house.food += piece
                self.house.money -= piece
                print('{} купила {} еды!'.format(self.name, piece))

    def buy_fur_coat(self):
        if self.house.money >= 150:
            self.richness -= 10
            self.happiness += 60
            self.number_fur_coats += 1
            self.house.money -= 150
            print('{} купила шубу!'.format(self.name))
        else:
            print('{} хотела купить шубу, но денег в доме нет!'.format(self.name))

    def clean_house(self):

        self.richness -= 10
        self.house.dirt -= 100
        if self.house.dirt < 0:
            self.house.dirt = 0
        print('{} убралась!'.format(self.name) if self.richness > 0 else
              '{} умерла убираясь!')

    def buy_food_cat(self):
        if self.house.money >= 60:
            piece = 60
            self.house.cat_food += piece
            self.house.money -= piece
            print('{} купила {} еды для кота!'.format(self.name, piece))
        else:
            piece = self.house.money // 2
            self.house.cat_food += piece
            self.house.money -= piece
            print('{} купила {} еды для кота!'.format(self.name, piece))


class Cat:

    def __init__(self, name=None, satiety=30, house=None):
        self.name = name
        self.satiety = satiety
        self.house = house

    def __str__(self):
        return 'Кот {}, сытость {}'.format(self.name, self.satiety)

    def eat(self):

        self.satiety += 20
        self.house.cat_food -= 10
        print('Кот {} кушает!'.format(self.name))

    def sleep(self):
        self.satiety -= 10
        print('Кот {} спит!'.format(self.name))

    def tear_Wallpaper(self):
        self.satiety -= 10
        self.house.dirt += 5
        print('Кот {} грязнит!'.format(self.name))

    def act(self):
        if self.satiety <= 0:
            print('{} умер...'.format(self.name))
            return False
        dice = randint(1, 3)
        if self.satiety < 20 and self.house.cat_food >= 10:
            self.eat()
        elif dice == 1:
            self.sleep()
        else:
            self.tear_Wallpaper()
        return True

    def go_to_house(self, house):
        self.satiety -= 10
        self.house = house
        print('{} вьехал в дом!'.format(self.name))


######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи


'''
home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
cat = Cat(name='Мурзик')
serge.go_to_house(home)
masha.go_to_house(home)
cat.go_to_house(home)
for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    home.dirt += 5
    a=serge.act()
    print(a)
    masha.act()
    cat.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(cat, color='cyan')
    cprint(home, color='cyan')
'''


# Кот может:
#   есть,+
#   спать,+
#   драть обои+
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)+
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)+
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов+
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.+
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов+


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,+
# степень счастья  - не меняется, всегда ==100 ;)+

class Child(Human):
    def __init__(self, name):
        super().__init__(name)
        self.happiness = 100

    def act(self):

        if not super().alive():
            if self.richness <= 10:
                self.eat()
            else:
                self.sleep()
            return True
        else:
            return False

    def eat(self):
        self.richness += 10
        self.house.food -= 10
        print('{} поел {} еды!'.format(self.name, 10))

    def sleep(self):
        print('{} уснул!'.format(self.name))


def chaos_of_days(quantity_food_day, quantity_money_day):
    N_day = set()
    K_day = set()
    while len(N_day) != quantity_food_day:
        N_day.add(randint(0, 365))

    while len(K_day) != quantity_money_day:
        K_day.add(randint(0, 365))

    return N_day, K_day


def life(N_day, K_day, salary=150):
    def result():
        cprint('================== Итоги ==================', color='red')
        cprint(home, color='yellow')
        cprint(serge, color='yellow')
        cprint(masha, color='yellow')
        cprint(cats[0], color='yellow')
        cprint(cats[1], color='yellow')
        cprint(cats[2], color='yellow')
        cprint(dima, color='yellow')

        cprint('\t\t\t\t Всего {} шуб!'.format(masha.number_fur_coats), color='yellow')
        cprint('===========================================', color='red')

    cprint('================Strat!==================', color='red')
    home = House()
    serge = Husband(name='Сережа', salary=salary)
    masha = Wife(name='Маша')
    dima = Child(name='Дима')
    cats = [Cat(name='Барсик', house=home), Cat(name='Даша', house=home), Cat(name='Витя', house=home)]

    dima.go_to_house(home)
    serge.go_to_house(home)
    masha.go_to_house(home)
    for cat in cats:
        cat.go_to_house(house=home)

    for day in range(365):
        cprint('================== День {} =================='.format(day), color='red')
        if day in N_day:
            home.food //= 2
            cprint('ПОЛОВИНЫ ЕДЫ ПРОПАЛО', color='blue')
        if day in K_day:
            home.money //= 2
            cprint('ПОЛОВИНЫ ДЕНЕГ ПРОПАЛО', color='blue')
        home.dirt += 5

        if all([serge.act(), masha.act(), dima.act(), cats[0].act(), cats[1].act(), cats[2].act()]):
            print('Все живы!')
        else:
            cprint('\n\n\t Исследование показало:', color='red')
            cprint('\n\t\t C 3 котами!\n\t Значение зарплаты 150', color='red')
            cprint('Nмакс={} раз в год вдруг пропало половина еды\n'
                   'Kмакс={} раз в год вдруг пропало половина денег '.format(len(N_day), len(K_day)), color='red')
            return False

        cprint(serge, color='cyan')
        cprint(masha, color='cyan')
        cprint(dima, color='cyan')
        for cat in cats:
            cprint(cat, color='cyan')
        cprint(home, color='cyan')

    result()
    return True


flag = True
for food_incidents in range(0, 6):
    for money_incidents in range(0, 6):
        N_day, K_day = chaos_of_days(food_incidents, money_incidents)

        flag = life(N_day, K_day)
        if not flag:
            break
    if not flag:
        break
if flag:
    cprint('\n\n\t\t C 3 котами!\n\t Значение зарплаты 150', color='red')
    cprint('>{} раз в год вдруг пропало половина еды\n'
           '>{} раз в год пропало половина денег '.format(len(N_day), len(K_day)), color='red')

# зачёт! 🚀

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
