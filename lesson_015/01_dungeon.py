# -*- coding: utf-8 -*-

# Подземелье было выкопано ящеро-подобными монстрами рядом с аномальной рекой, постоянно выходящей из берегов.
# Из-за этого подземелье регулярно затапливается, монстры выживают, но не герои, рискнувшие спуститься к ним в поисках
# приключений.
# Почуяв безнаказанность, ящеры начали совершать набеги на ближайшие деревни. На защиту всех деревень не хватило
# солдат и вас, как известного в этих краях героя, наняли для их спасения.
#
# Карта подземелья представляет собой json-файл под названием rpg.json. Каждая локация в лабиринте описывается объектом,
# в котором находится единственный ключ с названием, соответствующем формату "Location_<N>_tm<T>",
# где N - это номер локации (целое число), а T (вещественное число) - это время,
# которое необходимо для перехода в эту локацию. Например, если игрок заходит в локацию "Location_8_tm30000",
# то он тратит на это 30000 секунд.
# По данному ключу находится список, который содержит в себе строки с описанием монстров а также другие локации.
# Описание монстра представляет собой строку в формате "Mob_exp<K>_tm<M>", где K (целое число) - это количество опыта,
# которое получает игрок, уничтожив данного монстра, а M (вещественное число) - это время,
# которое потратит игрок для уничтожения данного монстра.
# Например, уничтожив монстра "Boss_exp10_tm20", игрок потратит 20 секунд и получит 10 единиц опыта.
# Гарантируется, что в начале пути будет две локации и один монстр
# (то есть в коренном json-объекте содержится список, содержащий два json-объекта, одного монстра и ничего больше).
#
# На прохождение игры игроку дается 123456.0987654321 секунд.
# Цель игры: за отведенное время найти выход ("Hatch")
#
# По мере прохождения вглубь подземелья, оно начинает затапливаться, поэтому
# в каждую локацию можно попасть только один раз,
# и выйти из нее нельзя (то есть двигаться можно только вперед).
#
# Чтобы открыть люк ("Hatch") и выбраться через него на поверхность, нужно иметь не менее 280 очков опыта.
# Если до открытия люка время заканчивается - герой задыхается и умирает, воскрешаясь перед входом в подземелье,
# готовый к следующей попытке (игра начинается заново).
#
# Гарантируется, что искомый путь только один, и будьте аккуратны в рассчетах!
# При неправильном использовании библиотеки decimal человек, играющий с вашим скриптом рискует никогда не найти путь.
#
# Также, при каждом ходе игрока ваш скрипт должен запоминать следущую информацию:
# - текущую локацию
# - текущее количество опыта
# - текущие дату и время (для этого используйте библиотеку datetime)
# После успешного или неуспешного завершения игры вам необходимо записать
# всю собранную информацию в csv файл dungeon.csv.
# Названия столбцов для csv файла: current_location, current_experience, current_date
#
#
# Пример взаимодействия с игроком:
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло времени: 00:00
#
# Внутри вы видите:
# — Вход в локацию: Location_1_tm1040
# — Вход в локацию: Location_2_tm123456
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали переход в локацию Location_2_tm1234567890
#
# Вы находитесь в Location_2_tm1234567890
# У вас 0 опыта и осталось 0.0987654321 секунд до наводнения
# Прошло времени: 20:00
#
# Внутри вы видите:
# — Монстра Mob_exp10_tm10
# — Вход в локацию: Location_3_tm55500
# — Вход в локацию: Location_4_tm66600
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали сражаться с монстром
#
# Вы находитесь в Location_2_tm0
# У вас 10 опыта и осталось -9.9012345679 секунд до наводнения
#
# Вы не успели открыть люк!!! НАВОДНЕНИЕ!!! Алярм!
#
# У вас темнеет в глазах... прощай, принцесса...
# Но что это?! Вы воскресли у входа в пещеру... Не зря матушка дала вам оберег :)
# Ну, на этот-то раз у вас все получится! Трепещите, монстры!
# Вы осторожно входите в пещеру... (текст умирания/воскрешения можно придумать свой ;)
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло уже 0:00:00
# Внутри вы видите:
#  ...
#  ...
#
# и так далее...
import csv
import json
import re

import os.path
import datetime
from decimal import *


# если изначально не писать число в виде строки - теряется точность!


class Game:
    ALL_TIME = '123456.0987654321'
    field_names = ['current_location', 'current_experience', 'current_date']

    def __init__(self, name_file='rpg.json'):
        self.name_file = name_file
        self.loaded_json_file = None
        self.name_lokation = None
        self.gameover_flag = False
        self.game_WIN_flag = False

        self.experience = 0
        self.remaining_time = Decimal('123456.0987654321')

        self.date = []

    def read_rpg_map(self):
        with open(self.name_file, "r") as read_file:
            self.loaded_json_file = json.load(read_file)

    def checking_file_for_existence(self):
        check_file = os.path.exists('rpg.csv')
        print(check_file)
        if not check_file:
            field_names = ['current_location', 'current_experience', 'current_date']
            with open('rpg.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(field_names)

    def start(self):
        self.checking_file_for_existence()
        self.read_rpg_map()
        self.go_first()
        while not self.gameover_flag:
            self.go()
        self.write_rpg_file()

    def write_rpg_file(self):

        with open('rpg.csv', 'a', newline='') as out_csv:
            writer = csv.writer(out_csv)  # <_csv.writer object at 0x03B0AD80>

            for row in self.date:
                writer.writerow(row)

    def go_first(self):
        for key in self.loaded_json_file.keys():
            self.name_lokation = key

        a = datetime.timedelta(seconds=float(self.remaining_time))
        self.date.append([self.name_lokation, self.experience, a])

    def go(self):
        print('=' * 72)
        print('|{:^70}|'.format(f"Вы находитесь в {self.name_lokation}"))
        print('|{:^70}|'.format(f'У вас {self.experience} опыта и осталось {self.remaining_time} секунд до наводнения'))
        print('=' * 72)
        monstrs = []
        locations = []
        print()
        print('|{:^70}|'.format("Внутри вы видите:"))
        for monstr in self.loaded_json_file[self.name_lokation]:
            if type(monstr) == dict:
                continue
            else:
                print('|{:^70}|'.format(f"— Монстра {monstr}"))
                monstrs.append(monstr)
        print()
        for i, location in enumerate(self.loaded_json_file[self.name_lokation]):
            if type(location) == str:
                # TODO Так сравнивать типы - это антипаттерн
                # TODO ИСпользуйте функцию isinstance(element, Class)
                # TODO (замените тут и ниже везде)
                continue
            else:
                for _location in location.keys():
                    print('|{:^70}|'.format(f"— Вход в локацию {_location}"))
                    locations.append([i, _location])

        if len(monstrs) == len(locations) == 0:
            print('|{:^70}|'.format(" Ничего! "))

        print()
        print('-' * 72)
        print('|{:^70}|'.format(" Выберите действие:"))
        print('-' * 72)

        print('|{:^70}|'.format("1.Атаковать монстра"))

        print('|{:^70}|'.format("2.Перейти в другую локацию или идти на ощупь, если ничего не видно!"))
        print('|{:^70}|'.format("3.Сдаться и выйти из игры"))
        print('-' * 72)
        key = int(input('Выбор:'))
        if key not in [1, 2, 3]:
            print()
            print("{:^70}".format("Всего 3 варианта!"))
            print()
        # TODO Очень длинный метод получается
        # TODO Можете ли вы разбить код по действиям
        # TODO Чтобы в идеале была структура
        #  if key == 1
        #      действие_1()
        #  elif key == 2
        #      действие_2()
        if key == 1:
            if monstrs == []:
                print()
                print("{:^70}".format("Тут врагов нет !"))
                print()
            else:
                monstr = monstrs[0]
                # monstr_pattern = r'Boss_exp|Mob_exp[0:999]_tm[0:999]'
                pars = re.split(r'_tm', monstr)
                time = pars[1]
                exp = re.split(r'_exp', pars[0])[1]
                self.time_processing(time=time)
                self.exp_processinf(exp=exp)
                self.loaded_json_file[self.name_lokation].remove(monstr)
        if key == 2:
            if not self.game_over(locations):
                if locations == []:
                    print()
                    print("{:^70}".format('Очень жаль, это тупик! Назад ходить нельзя!'))
                    print("{:^70}".format("YOU DIED"))
                    print()
                    self.gameover_flag = True
                else:
                    key_location = input("Введите номер локации: Location_?_tm..  ?=")
                    location_pattern = f'Location_{key_location}_tm'
                    flag_correctnesses = False
                    for loc in locations:
                        if location_pattern in loc[1]:
                            print()

                            # print("Добро пожаловать в ", loc[1])
                            time = loc[1][len(location_pattern):]
                            self.time_processing(time=time)
                            self.loaded_json_file = self.loaded_json_file[self.name_lokation][loc[0]]
                            self.name_lokation = loc[1]
                            flag_correctnesses = True
                    if not flag_correctnesses:
                        print()
                        print("{:^70}".format("Такого вариан!"))
                        print()



            else:
                self.gameover_flag = True

        if key == 3:
            self.gameover_flag = True
            print('{:^70}'.format('Вы проиграли'))
            self.write_rpg_file()
            exit()
        a = datetime.timedelta(seconds=float(self.remaining_time))
        self.date.append([self.name_lokation, self.experience, a])

    def time_processing(self, time):
        print("!" + '=' * 70 + "!")
        print('!{:^70}!'.format(f'Потратили {time} c '))
        print('!{:^70}!'.format(f"Осталось {self.remaining_time - Decimal(time)} c "))
        self.remaining_time -= Decimal(time)
        print("!" + '=' * 70 + "!")

    def exp_processinf(self, exp):
        self.experience += int(exp)
        print('!{:^70}!'.format(f'Убили монстра! Получили {exp} опыта'))
        print("!" + '=' * 70 + "!")
        print()

    def game_over(self, locations):
        for loc in locations:
            if loc[1] == "Hatch_tm159.098765432" and self.experience >= 280:
                print()
                print("{:^70}".format("WINNER!"))
                self.game_WIN_flag = True
                return True
            elif loc[1] == "Hatch_tm159.098765432" and not self.experience >= 280:
                print()
                print("|{:^70}|".format(
                    f"Вы добрались до люка! Но нет сил открыть его, всего опыта exp ={self.experience}!"))
                print("{:^70}".format("YOU DIED"))
                return True

        return False


if __name__ == "__main__":
    # TODO в идеале нужно весь этот код занести внутрь класса
    # TODO чтобы тут остались только инициализация класса и запуск одного метода
    getcontext().prec = 50
    count = 1
    game_WIN_flag = False
    while not game_WIN_flag:
        print("{:^70}".format(f'Жизнь {count}'))
        game = Game()
        game.start()
        game_WIN_flag = game.game_WIN_flag
        count += 1

    print("{:^70}".format(f'Ураа!!!!'))
    print("{:^70}".format(f'Всего {count} попыток!'))
# Учитывая время и опыт, не забывайте о точности вычислений!
