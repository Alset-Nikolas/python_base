# -*- coding: utf-8 -*-

import os
import time

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


class FilesArrange:
    def __init__(self, zip_name, path):
        self.zip_name = zip_name
        self.path_unpack_dir = path
        self.data = []

    def unpacking_zip_file(self):
        if not os.path.exists(self.path_unpack_dir):
            self.zfile = zipfile.ZipFile(self.zip_name, 'r')
            self.txt_name_file = self.zfile.namelist()[0]
            for filename in self.zfile.namelist():
                self.zfile.extract(filename)
            print(f'Распаковка файла завершена! Появился файл "{self.txt_name_file}"')
        else:
            self.zfile = zipfile.ZipFile(self.zip_name, 'r')

        self.path_unpack_dir = self.normpath(self.path_unpack_dir)

    def normpath(self, path):
        return os.path.normpath(path)

    def walk_in_old_dir(self):
        for dirpath, dirnames, filenames in os.walk(self.path_unpack_dir):
            if filenames:
                for name_foto in filenames:
                    all_dir_path = os.path.join(dirpath, name_foto)
                    date = time.gmtime(os.path.getmtime(all_dir_path))
                    time_ = list(date[:6])
                    self.data.append([all_dir_path, time_, name_foto])

    def create(self, new_path):
        # создать пустой каталог (папку)
        self.new_path_main_dir = new_path
        if not os.path.isdir(self.new_path_main_dir):
            os.mkdir(self.new_path_main_dir)

    def func_sort_file(self):
        for old_path_photo, time_, name_foto in self.data:
            new_name_year_dirs = os.path.join(self.new_path_main_dir,str(time_[0])+' Year')
            new_name_month_dirs = os.path.join(new_name_year_dirs,str(time_[1])+' Month')
            if not os.path.isdir(new_name_year_dirs):
                os.makedirs(new_name_year_dirs)
            if not os.path.isdir(new_name_month_dirs):
                os.makedirs(new_name_month_dirs)
            self.move_func_sort_file(new_name_month_dirs=new_name_month_dirs, name_foto=name_foto,
                                     old_path_photo=old_path_photo)

    def move_func_sort_file(self, new_name_month_dirs, name_foto, old_path_photo):
        # заменить (переместить) этот файл в другой каталог
        text = os.path.join(new_name_month_dirs, name_foto)
        os.replace(old_path_photo, text)


zip_name = 'icons.zip'
A = FilesArrange(zip_name=zip_name, path='icons')
A.unpacking_zip_file()
A.walk_in_old_dir()
A.create(new_path='icons_by_year')
A.func_sort_file()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html

