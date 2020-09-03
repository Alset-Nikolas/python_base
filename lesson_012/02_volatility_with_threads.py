# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#

import threading

import csv
import math
import zipfile

# TODO во всех названиях, где встречается tiker - допущена ошибка. Должно быть ticker

class ParsFile(threading.Thread):  # TODO должно быть ParseFile
    def __init__(self, name_file,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name_file = name_file

    def run(self):
        with open(self.name_file) as File:
            reader = csv.reader(File)
            max_price_tiker, min_price_tiker = self.search_max_min_tiker(reader)
        half_sum_tiker = (max_price_tiker + min_price_tiker) / 2
        volatility_tiker = ((max_price_tiker - min_price_tiker) / half_sum_tiker) * 100

        self.volatility_tiker = volatility_tiker

    def search_max_min_tiker(self, reader):
        max_price_tiker = -math.inf
        min_price_tiker = math.inf
        for row in reader:
            if row == ['SECID', 'TRADETIME', 'PRICE', 'QUANTITY']:
                continue
            self.name_tiker = row[0]
            max_price_tiker = max(max_price_tiker, float(row[2]))
            min_price_tiker = min(min_price_tiker, float(row[2]))
        return max_price_tiker, min_price_tiker

class ExtractZiFile:
    def __init__(self, file_zip_path_downloaded):
        self.file_zip_path_downloaded = file_zip_path_downloaded
        self.names_file = []

    def extract_zip_file(self):
        self.checking_name_file()
        for name_file in self.zip.namelist():
            self.zip.extract(member=name_file)
            if name_file[-4:] == '.csv':
                self.names_file.append(name_file)


    def checking_name_file(self):
        try:
            self.zip = zipfile.ZipFile(file=self.file_zip_path_downloaded, mode='r')
        except Exception as e:
            print(e)



file_zip_path_downloaded = 'trades.zip'
zip_open = ExtractZiFile(file_zip_path_downloaded=file_zip_path_downloaded)
zip_open.extract_zip_file()


class Manager:
    def __init__(self, names_file):
        self.names_file = names_file
        self.date = []
        self.date_volatility_tiker_0 = []

    def main(self):
        parsers = [ParsFile(name) for name in self.names_file]
        for parser in parsers:
            parser.start()
        for parser in parsers:
            parser.join()
            if parser.volatility_tiker == 0:
                self.date_volatility_tiker_0.append(parser.name_tiker)
            else:
                self.date.append([parser.name_tiker, parser.volatility_tiker])
        self.ssort()
        self.pprint()

    def ssort(self):
        self.date.sort(key=lambda x: x[1], reverse=True)
        self.date_volatility_tiker_0.sort()

    def pprint(self):

        print('Максимальная волатильность:')
        for line in self.date[:3]:
            print(f'{line[0]} - {round(line[1], 2)} %')

        print('\nМинимальная волатильность:')
        for line in self.date[-3:]:
            print(f'{line[0]} - {round(line[1], 2)} %')

        print('\nНулевая волатильность:')
        for line in self.date_volatility_tiker_0:
            print(f'{line}', end=', ')
        # TODO последний элемент в этом цикле распечатать так, чтобы запятая в конце строки не подставлялось:
        #  CLM9, CYH9, EDU9, EuH0, EuZ9, JPM9, MTM9, O4H9, PDU9, PTU9, RIH0, RRG9, TRH9, VIH9,



A = Manager(zip_open.names_file)
A.main()
# TODO оформить код по PEP8
