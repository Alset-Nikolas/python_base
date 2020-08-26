# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4
import os
import zipfile


class Statistics:

    def __init__(self, zip_name):
        self.zip_name = zip_name
        self.alfavit = {}
        self.stat = []
        self.txt_name_file = None

    def unpacking_zip_file(self):
        ''' voina-i-mur.zip ---> voina-i-mur.txt'''
        os.path.normpath(self.zip_name)
        self.zfile = zipfile.ZipFile(self.zip_name, 'r')
        self.txt_name_file = self.zfile.namelist()[0]
        for filename in self.zfile.namelist():
            self.zfile.extract(filename)
        print(f'Распаковка файла завершена! Появился файл "{self.txt_name_file}"')

    def stat_alfavit(self):
        '''Статиcтика алфавита!'''
        self.creation_alphabet()
        with open(self.txt_name_file, 'r', encoding='cp1251') as file:
            for line in file:
                for symbol in line:
                    if 'а' <= symbol <= 'я' or 'А' <= symbol <= 'Я':
                        self.alfavit[symbol] += 1

    def creation_alphabet(self):
        '''Создать алфавит'''
        for x in range(ord('А'), ord('Я') + 1):
            self.alfavit[chr(x)] = 0
        for x in range(ord('а'), ord('я') + 1):
            self.alfavit[chr(x)] = 0

    def sort_stat(self):
        '''Сортировка статистики'''
        for key, value in self.alfavit.items():
            self.stat.append((key, value))

        for _ in range(len(self.stat)):
            for x in range(len(self.stat) - 1):
                if self.stat[x][1] < self.stat[x + 1][1]:
                    self.stat[x + 1], self.stat[x] = self.stat[x], self.stat[x + 1]

    def p_print(self):
        '''Вывод на экран'''
        all_number = 0
        for letter, number in self.stat:
            print('\t+---------+----------+')
            print('\t|{:^9}'.format(letter), '|{:^10}|'.format(number), sep='')
            all_number += number
        else:
            print('\t+---------+----------+')
            print('\t|{:^9}'.format('Итого'), '|{:^10}|'.format(all_number), sep='')
            print('\t+---------+----------+')


zip_name = 'python_snippets/voyna-i-mir.txt.zip'

A = Statistics(zip_name=zip_name)
A.unpacking_zip_file()
A.stat_alfavit()
A.sort_stat()
A.p_print()


class StatisticsFrequencyIncreases(Statistics):
    def sort_stat(self):
        '''Сортировка статистики по частоте по возрастанию'''
        for key, value in self.alfavit.items():
            self.stat.append((key, value))

        for _ in range(len(self.stat)):
            for x in range(len(self.stat) - 1):
                if self.stat[x][1] > self.stat[x + 1][1]:
                    self.stat[x + 1], self.stat[x] = self.stat[x], self.stat[x + 1]


A = StatisticsFrequencyIncreases(zip_name=zip_name)
A.unpacking_zip_file()
A.stat_alfavit()
A.sort_stat()
A.p_print()


class StatisticsABC(Statistics):

    def sort_stat(self):
        '''Сортировка статистики по алфавиту по убыванию'''
        for key, value in self.alfavit.items():
            self.stat.append((key, value))

        for _ in range(len(self.stat)):
            for x in range(len(self.stat) - 1):
                if self.stat[x][0] > self.stat[x + 1][0]:
                    self.stat[x + 1], self.stat[x] = self.stat[x], self.stat[x + 1]


A = StatisticsABC(zip_name=zip_name)
A.unpacking_zip_file()
A.stat_alfavit()
A.sort_stat()
A.p_print()


class StatisticsABCIncreases(Statistics):

    def sort_stat(self):
        '''Сортировка статистики по алфавиту по возрастанию'''
        for key, value in self.alfavit.items():
            self.stat.append((key, value))

        for _ in range(len(self.stat)):
            for x in range(len(self.stat) - 1):
                if self.stat[x][0] < self.stat[x + 1][0]:
                    self.stat[x + 1], self.stat[x] = self.stat[x], self.stat[x + 1]


A = StatisticsABCIncreases(zip_name=zip_name)
A.unpacking_zip_file()
A.stat_alfavit()
A.sort_stat()
A.p_print()

# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию+
#  - по алфавиту по возрастанию+
#  - по алфавиту по убыванию+

# зачёт! 🚀
