# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>  # Итератор или генератор? выбирайте что вам более понятно
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234


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

    def write_file(self):
        x = 0
        while x != len(self.data):
            yield ('{}-{:02d}-{:02d} {:02d}:{:02d} {}\n'.format(*self.data[x], self.data.count(self.data[x])))
            x += self.data.count(self.data[x])


A = ParsTxtFile(txt_name_file='events.txt')
A.read_the_file()
for line in A.write_file():
    print(line, end='')
