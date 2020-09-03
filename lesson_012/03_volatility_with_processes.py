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
import csv
import math
import zipfile


class ParseFile(multiprocessing.Process):
    def __init__(self, name_file, collector, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name_file = name_file
        self.collector = collector
        self.name_ticker = None

    def run(self):
        with open(self.name_file) as File:
            reader = csv.reader(File)
            max_price_ticker, min_price_ticker = self.search_max_min_ticker(reader)
        half_sum_ticker = (max_price_ticker + min_price_ticker) / 2
        volatility_ticker = ((max_price_ticker - min_price_ticker) / half_sum_ticker) * 100

        self.volatility_ticker = volatility_ticker
        self.collector.put([self.name_ticker, volatility_ticker])

    def search_max_min_ticker(self, reader):
        max_price_ticker = -math.inf
        min_price_ticker = math.inf
        for i, row in enumerate(reader):

            if row == ['SECID', 'TRADETIME', 'PRICE', 'QUANTITY']:
                continue
            self.name_ticker = row[0]
            try:
                max_price_ticker = max(max_price_ticker, float(row[2]))
                min_price_ticker = min(min_price_ticker, float(row[2]))
            except:
                print(row)
                print('-------------=============------------------')

        return max_price_ticker, min_price_ticker


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


class Manager(multiprocessing.Process):
    def __init__(self, names_file, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.names_file = names_file
        self.date = []
        self.date_volatility_ticker_0 = []
        self.collector = multiprocessing.Queue()

    def run(self):
        parsers = [ParseFile(name, self.collector) for name in self.names_file]
        for parser in parsers:
            parser.start()
        pam = 1
        while any(parser.is_alive() for parser in parsers):
            [name_ticker, volatility_ticker] = self.collector.get()
            pam += 1
            if volatility_ticker == 0:
                self.date_volatility_ticker_0.append(name_ticker)
            else:
                self.date.append([name_ticker, volatility_ticker])
            if pam == len(self.names_file):
                break

        for parser in parsers:
            parser.join()

        self.ssort()
        self.pprint()

    def ssort(self):
        self.date.sort(key=lambda x: x[1], reverse=True)
        self.date_volatility_ticker_0.sort()

    def pprint(self):

        print('Максимальная волатильность:')
        for line in self.date[:3]:
            print(f'{line[0]} - {round(line[1], 2)} %')

        print('\nМинимальная волатильность:')
        for line in self.date[-3:]:
            print(f'{line[0]} - {round(line[1], 2)} %')

        print('\nНулевая волатильность:')
        for line in self.date_volatility_ticker_0:
            if line != self.date_volatility_ticker_0[-1]:
                print(f'{line}', end=', ')
            else:
                print(f'{line}')


if __name__ == '__main__':
    file_zip_path_downloaded = 'trades.zip'
    zip_open = ExtractZiFile(file_zip_path_downloaded=file_zip_path_downloaded)
    zip_open.extract_zip_file()

    A = Manager(zip_open.names_file)
    A.start()
    A.join()
