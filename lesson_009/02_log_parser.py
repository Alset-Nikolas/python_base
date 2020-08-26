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

class ParsTxtFile:

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


class ParsTxtFileHour(ParsTxtFile):
    def write_file(self, out_txt_file):
        with open(out_txt_file, 'w') as file:
            early_line = None
            count_line = 0
            for line in self.data:
                _line = line[:-1]
                if early_line is None:
                    early_line = _line
                elif early_line == _line:
                    count_line += 1
                elif early_line != _line:
                    file.write(
                        '{}-{:02d}-{:02d} {:02d} {}\n'.format(*_line, count_line))
                    count_line = 1
                    early_line = _line


class ParsTxtFileMonth(ParsTxtFile):

    def write_file(self, out_txt_file):
        with open(out_txt_file, 'w') as file:
            early_line = None
            count_line = 0
            for line in self.data:
                _line = line[:2]
                if early_line is None:
                    early_line = _line
                elif early_line == _line:
                    count_line += 1
                elif early_line != _line:
                    file.write(
                        '{}-{:02d} {}\n'.format(*_line, count_line))
                    count_line = 1
                    early_line = _line
                if count_line == len(self.data) - 1:
                    file.write(
                        '{}-{:02d} {}\n'.format(*_line, count_line))


class ParsTxtFileYear(ParsTxtFile):

    def write_file(self, out_txt_file):
        with open(out_txt_file, 'w') as file:
            early_line = None
            count_line = 0
            for line in self.data:
                _line = line[:1]
                if early_line is None:
                    early_line = _line
                elif early_line == _line:
                    count_line += 1
                elif early_line != _line:
                    file.write(
                        '{} {}\n'.format(*_line, count_line))
                    count_line = 1
                    early_line = _line
                if count_line == len(self.data) - 1:
                    file.write(
                        '{} {}\n'.format(*_line, count_line))


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
    A = ParsTxtFile(txt_name_file='events.txt')
    A.read_the_file()
    A.write_file(out_txt_file='out_parses.txt')
elif N == '2':
    A = ParsTxtFileHour(txt_name_file='events.txt')
    A.read_the_file()
    A.write_file(out_txt_file='out_parses.txt')
elif N == '3':
    A = ParsTxtFileMonth(txt_name_file='events.txt')
    A.read_the_file()
    A.write_file(out_txt_file='out_parses.txt')
elif N == '4':
    A = ParsTxtFileYear(txt_name_file='events.txt')
    A.read_the_file()
    A.write_file(out_txt_file='out_parses.txt')
print('Все!')

# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году

# зачёт! 🚀
