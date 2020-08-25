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

class Pars_Txt_File:  # TODO имена классов принято задавать в CamelCase. То есть Pars_Txt_File -> ParsTxtFile

    def __init__(self, txt_name_file):
        self.txt_name_file = txt_name_file
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

    def write_file(self, out_txt_file):

        with open(out_txt_file, 'w') as file:
            x = 0
            while x != len(self.data):
                file.write('{}-{:02d}-{:02d} {:02d}:{:02d} {}\n'.format(*self.data[x], self.data.count(self.data[x])))
                x += self.data.count(self.data[x])


# TODO убрать дублирующийся код метода из классов-наследников
class Pars_Txt_File_Hour(Pars_Txt_File):  # TODO см. замечание выше
    def parsing_line(self, line):
        year = int(line[1:5])
        month = int(line[6:8])
        day = int(line[9:11])
        hour = int(line[12:14])
        value = line[-4:-1]
        return [year, month, day, hour], value

    def write_file(self, out_txt_file):
        with open(out_txt_file, 'w') as file:
            x = 0
            while x != len(self.data):
                file.write('{}-{:02d}-{:02d} {:02d} {}\n'.format(*self.data[x], self.data.count(self.data[x])))
                x += self.data.count(self.data[x])


class Pars_Txt_File_Month(Pars_Txt_File):
    def parsing_line(self, line):
        year = int(line[1:5])
        month = int(line[6:8])
        value = line[-4:-1]
        return [year, month], value

    def write_file(self, out_txt_file):
        with open(out_txt_file, 'w') as file:
            x = 0
            while x != len(self.data):
                file.write('{}-{:02d} {}\n'.format(*self.data[x], self.data.count(self.data[x])))
                x += self.data.count(self.data[x])


class Pars_Txt_File_Year(Pars_Txt_File):
    def parsing_line(self, line):
        year = int(line[1:5])
        value = line[-4:-1]
        return [year], value

    def write_file(self, out_txt_file):
        with open(out_txt_file, 'w') as file:
            x = 0
            while x != len(self.data):
                file.write('{} {}\n'.format(*self.data[x], self.data.count(self.data[x])))
                x += self.data.count(self.data[x])


while True:
    print('Какую сделать группировку событий?')
    print('1->за каждую минуту')
    print('2->по часам')
    print('3->по месяцу')
    print('4->по году')
    N = input()
    if N in {'1', '2', '3', '4'}:
        break
    else:
        print('Всего 4 варианта!')

if N == '1':
    A = Pars_Txt_File(txt_name_file='events.txt')
    A.read_the_file()
    A.write_file(out_txt_file='out_parses.txt')
elif N == '2':
    A = Pars_Txt_File_Hour(txt_name_file='events.txt')
    A.read_the_file()
    A.write_file(out_txt_file='out_parses.txt')
elif N == '3':
    A = Pars_Txt_File_Month(txt_name_file='events.txt')
    A.read_the_file()
    A.write_file(out_txt_file='out_parses.txt')
elif N == '4':
    A = Pars_Txt_File_Year(txt_name_file='events.txt')
    A.read_the_file()
    A.write_file(out_txt_file='out_parses.txt')
print('Все!')

# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
