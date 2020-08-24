# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4
from pprint import pprint
# TODO нужен ли этот импорт?

# TODO оформить код по PEP8
class pars_txt_file:  # TODO названия классов должны быть с заглавной буквы (и в CamelCase)

    def __init__(self):
        self.txt_name_file = 'events.txt'  # TODO это значение должно приходить из аргумента в конструкторе класса
        self.data = []

    def parsing_line(self, line):
        year = int(line[1:5])
        month = int(line[6:8])
        day = int(line[9:11])
        hour = int(line[12:14])
        minute = int(line[15:17])
        value = line[-4:-1]
        return [year, month, day, hour, minute], value





    def read_the_file(self):

        with open(self.txt_name_file, 'r', encoding='cp1251') as file:
            count = 0
            for line in file:
                pars, value = self.parsing_line(line)
                if value == ' OK':
                    continue
                else:
                    self.data.append(pars)


    def write_file(self):

        with open('out_parses.tx.', 'w') as file:  # TODO имя выходного файла тоже должно задаваться через аргумент
            # TODO в формате файла допущена ошибка
            x=0
            while x != len(self.data):
                file.write('{} {}\n'.format(self.data[x], self.data.count(self.data[x])))
                x +=self.data.count(self.data[x])


A = pars_txt_file()
A.read_the_file()
A.write_file()

# TODO названия классов должны быть с заглавной буквы (и в CamelCase)
class pars_txt_file_hour(pars_txt_file):
    def parsing_line(self, line):
        year = int(line[1:5])
        month = int(line[6:8])
        day = int(line[9:11])
        hour = int(line[12:14])
        value = line[-4:-1]
        return [year, month, day, hour], value

class pars_txt_file_day(pars_txt_file):
    def parsing_line(self, line):
        year = int(line[1:5])
        month = int(line[6:8])
        day = int(line[9:11])
        value = line[-4:-1]
        return [year, month, day], value
    
class pars_txt_file_month(pars_txt_file):
    def parsing_line(self, line):
        year = int(line[1:5])
        month = int(line[6:8])
        value = line[-4:-1]
        return [year, month], value
    
class pars_txt_file_year(pars_txt_file):
    def parsing_line(self, line):
        year = int(line[1:5])
        value = line[-4:-1]
        return year, value

# TODO реализовать вызовы шаблонных методов для демонстрации их работы

# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
