# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от полусуммы крайних значений цены за торговую сессию:
#   полусумма = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / полусумма) * 100%
# Например для бумаги №1:
#   half_sum = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / half_sum) * 100 = 8.7%
# Для бумаги №2:
#   half_sum = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / half_sum) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
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
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>

import csv
import math
import zipfile


class ParsTicker:

    def __init__(self, file_zip_path_downloaded):
        self.file_zip_path_downloaded = file_zip_path_downloaded

        self.date = []
        self.date_volatility_ticker_0 = []

    def run(self):
        self.extract_zip_file()
        self.print_result()

    def checking_name_file(self):
        try:
            self.zip = zipfile.ZipFile(file=self.file_zip_path_downloaded, mode='r')
        except Exception as e:
            print(e)

    def extract_zip_file(self):
        self.checking_name_file()
        for name_file in self.zip.namelist():
            self.zip.extract(member=name_file)

            self.parse_csv_file(name_file)

    def parse_csv_file(self, name_file):
        if name_file[-4:] == '.csv':
            with open(name_file) as File:
                reader = csv.reader(File)
                name_ticker, max_price_ticker, min_price_ticker = self.search_max_min_ticker(reader)
            half_sum_ticker = (max_price_ticker + min_price_ticker) / 2
            volatility_ticker = ((max_price_ticker - min_price_ticker) / half_sum_ticker) * 100
            if volatility_ticker == 0:
                self.date_volatility_ticker_0.append(name_ticker)
            else:
                self.date.append([name_ticker, volatility_ticker])
            self.sort_date()

    def search_max_min_ticker(self, reader):
        max_price_ticker = -math.inf
        min_price_ticker = math.inf
        for row in reader:
            if row == ['SECID', 'TRADETIME', 'PRICE', 'QUANTITY']:
                continue
            name_ticker = row[0]
            max_price_ticker = max(max_price_ticker, float(row[2]))
            min_price_ticker = min(min_price_ticker, float(row[2]))
        return name_ticker, max_price_ticker, min_price_ticker

    def sort_date(self):
        self.date.sort(key=lambda x: x[1], reverse=True)
        self.date_volatility_ticker_0.sort()

    def print_result(self):
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


file_zip_path_downloaded = 'trades.zip'
A = ParsTicker(file_zip_path_downloaded=file_zip_path_downloaded)
A.run()
#зачёт!