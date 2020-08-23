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

import zipfile
from pprint import pprint


def unpacking_zip_file(zip_name):
    ''' voina-i-mur.zip ---> voina-i-mur.txt'''

    zfile = zipfile.ZipFile(zip_name, 'r')
    txt_name_file = zfile.namelist()[0]
    for filename in zfile.namelist():
        zfile.extract(filename)
    print(f'Распаковка файла завершена! Появился файл "{txt_name_file}"')
    return txt_name_file


zip_name = 'C:\\Users\\User\\PycharmProjects\\python_base\\lesson_009\\python_snippets\\voyna-i-mir.txt.zip'
txt_name_file = unpacking_zip_file(zip_name=zip_name)

def stat_alfavit():
    alfavit = {}

    for x in range(ord('А'), ord('Я') + 1):
        alfavit[chr(x)] = 0
    for x in range(ord('а'), ord('я') + 1):
        alfavit[chr(x)] = 0


    with open(txt_name_file, 'r', encoding='cp1251') as file:
        for line in file:
            for symbol in line:
                if 'а' <= symbol <= 'я' or 'А' <= symbol <= 'Я':
                    alfavit[symbol] += 1

    return alfavit

alfavit = stat_alfavit()

def sort_stat(alfavit):
    stat = []
    for key, value in alfavit.items():
        stat.append((key, value))

    for _ in range(len(stat)):
        for x in range(len(stat)-1):
            if stat[x][1] < stat[x+1][1]:
                stat[x+1], stat[x] = stat[x], stat[x+1]
    return stat
stat = sort_stat(alfavit)


def p_print(stat):
    for letter, number in stat:
        print('+---------+----------+')
        print('|{:^9}'.format(letter), '|{:^10}|'.format(number), sep='')
    else:
        print('+---------+----------+')
p_print(stat)
# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
