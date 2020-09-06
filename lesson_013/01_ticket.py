# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

from PIL import Image, ImageDraw, ImageFont, ImageColor
import argparse
import os


def make_ticket(fio='Иванов И.И.', from_='Земля', to='Луна', date='09.12', path_save='\\image.png'):
    path_ticket_template = os.path.normpath(path_dir + '\\images\\ticket_template.png')
    path_ofont = os.path.join(path_dir, 'ofont.ru_Schula.ttf')
    path_save_file = os.path.normpath(path_dir + path_save)
    print(path_ticket_template)
    print(path_ofont)
    print(path_save_file)

    image = Image.open(path_ticket_template)
    idraw = ImageDraw.Draw(image)

    font = ImageFont.truetype(path_ofont, size=14)

    X_SIZE = image.size[0]
    Y_SIZE = image.size[1]

    x_fio = X_SIZE // 7
    x_from_ = X_SIZE // 10
    x_to = x_from_
    x_date = X_SIZE // 2 - 50
    y_fio = Y_SIZE // 3 - 5
    y_from_ = Y_SIZE // 2 - 3
    y_to = Y_SIZE // 2 + Y_SIZE // 6 - 3
    y_date = y_to

    idraw.text((x_date, y_date), date, font=font, fill=ImageColor.colormap['black'])
    idraw.text((x_to, y_to), to, font=font, fill=ImageColor.colormap['black'])
    idraw.text((x_fio, y_fio), fio, font=font, fill=ImageColor.colormap['black'])
    idraw.text((x_from_, y_from_), from_, font=font, fill=ImageColor.colormap['black'])

    image.save(path_save_file)
    image.show()


all_path = __file__
name_file = os.path.basename(__file__)

path_dir = all_path[:-len(name_file) - 1]
path_dir = os.path.normpath(path_dir)

parser = argparse.ArgumentParser(description='Ping script')

parser.add_argument('--fio', action="store", dest='fio', help="Enter name!", default='None')
parser.add_argument('--from', action="store", dest='from_', help="Enter from where!", default='None')
parser.add_argument('--to', action="store", dest='to', help="Enter where!", default='None')
parser.add_argument('--date', action="store", dest='date', help="Enter Date!", default='None')

parser.add_argument('--save_to', action="store", dest="path", default='image.png', type=str,
                    help="Where to save?")

args = parser.parse_args()
print(args)

make_ticket(fio=args.fio, from_=args.from_, to=args.to, date=args.date, path_save='\\' + args.path)

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
