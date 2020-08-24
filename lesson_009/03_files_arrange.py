# -*- coding: utf-8 -*-

import os
import time
import shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.

# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени последней модификации файла
# (время создания файла берется по разному в разых ОС - см https://clck.ru/PBCAX - поэтому берем время модификации).
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником ОС в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит, см .gitignore в папке ДЗ)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4
import zipfile

import os.path


class files_arrange:
    def __init__(self, zip_name):
        self.zip_name = zip_name
        # TODO значение path должно приходить из аргумента в конструкторе класса
        self.path = 'C:\\Users\\User\\PycharmProjects\\python_base\\lesson_009\\icons'
        # TODO путь должен быть относительным и поддерживаемым на любых платформах (а не только на Вашем ПК и в Windows)
        self.data = []

    def unpacking_zip_file(self):
        if not os.path.exists("icons"):
            self.zfile = zipfile.ZipFile(zip_name, 'r')
            self.txt_name_file = self.zfile.namelist()[0]
            for filename in self.zfile.namelist():
                self.zfile.extract(filename)
            print(f'Распаковка файла завершена! Появился файл "{self.txt_name_file}"')

    def normpath(self):
        os.path.normpath(self.path)

    def walk_in_file(self):
        for dirpath, dirnames, filenames in os.walk(self.path):
            if filenames:
                for foto in filenames:
                    all_dir_path = os.path.join(dirpath, foto)
                    date = time.gmtime(os.path.getmtime(self.path))
                    self.data.append([all_dir_path, list(date[:6]), foto])

        sorted(self.data, key=lambda date_: date_[1][1])
        sorted(self.data, key=lambda date_: date_[1][0])

    def create(self):
        # создать пустой каталог (папку)
        if not os.path.isdir("icons_by_year"):
            os.mkdir("icons_by_year")

    def move(self):
        # заменить (переместить) этот файл в другой каталог
        for path in self.data:
            print(path[0])
            text = os.path.join('C:\\Users\\User\\PycharmProjects\\python_base\\lesson_009\\icons_by_year', path[2])
            # TODO путь до выходной директории тоже должен задаваться через аргумент и быть относительным
            os.replace(path[0], text)


zip_name = 'C:\\Users\\User\\PycharmProjects\\python_base\\lesson_009\\icons.zip'  # TODO путь должен быть относительным
A = files_arrange(zip_name=zip_name)
A.unpacking_zip_file()
A.normpath()
A.walk_in_file()
A.create()
A.move()

'''

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
    # Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
'''
