# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
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
import multiprocessing
import threading

import csv
import math
import zipfile


class ParsFile(multiprocessing.Process):
    def __init__(self, name_file, collector, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name_file = name_file
        self.collector = collector
        self.name_tiker = None

    def run(self):
        with open(self.name_file) as File:
            reader = csv.reader(File)
            max_price_tiker, min_price_tiker = self.search_max_min_tiker(reader)
        half_sum_tiker = (max_price_tiker + min_price_tiker) / 2
        volatility_tiker = ((max_price_tiker - min_price_tiker) / half_sum_tiker) * 100

        self.volatility_tiker = volatility_tiker
        self.collector.put([self.name_tiker, volatility_tiker])



    def search_max_min_tiker(self, reader):
        max_price_tiker = -math.inf
        min_price_tiker = math.inf
        for i, row in enumerate(reader):
            if row == ['SECID', 'TRADETIME', 'PRICE', 'QUANTITY']:
                continue
            self.name_tiker = row[0]
            try:
                max_price_tiker = max(max_price_tiker, float(row[2]))
                min_price_tiker = min(min_price_tiker, float(row[2]))
            except Exception as e:
                print(e)
                print(row, i)
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
    def __init__(self, names_file, collector):
        self.names_file = names_file
        self.date = []
        self.date_volatility_tiker_0 = []
        self.collector = collector


    def main(self):
        parsers = [ParsFile(name, collector) for name in self.names_file]
        for parser in parsers:
            parser.start()
        while True:
            try:
                [name_tiker, volatility_tiker] = self.collector.get()
                print([name_tiker, volatility_tiker])
                if volatility_tiker == 0:
                    self.date_volatility_tiker_0.append(name_tiker)
                else:
                    self.date.append([name_tiker, volatility_tiker])
            except self.collector.Empty:
                print('---------------пусто------------')
                if not any(parser.is_alive() for parser in parsers):
                    print(self.date)
                    break
        for parser in parsers:
            parser.join()

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


if __name__ =='__main__':
    collector = multiprocessing.Queue()
    A = Manager(zip_open.names_file, collector)
    A.main()