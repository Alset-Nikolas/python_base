# -*- coding: utf-8 -*-

# Прибежал менеджер и сказал что нужно срочно изменить правила подсчета очков в игре.
# "Выходим на внешний рынок, а там правила игры другие!" - сказал он.
#
# Правила подсчета очков изменяются так:
#
# Если во фрейме страйк, сумма очков за этот фрейм будет равна количеству сбитых кеглей в этом фрейме (10 кеглей)
# плюс количество фактически сбитых кеглей за два следующих броска шара (в одном или двух фреймах,
# в зависимости от того, был ли страйк в следующем броске).
# Например: первый бросок шара после страйка - тоже страйк, то +10 (сбил 10 кеглей)
# и второй бросок шара - сбил 2 кегли (не страйк, не важно как закончится этот фрейм - считаем кегли) - то еще +2.
#
# Если во фрейме сбит спэр, то сумма очков будет равна количеству сбитых кеглей в этом фрейме (10 кеглей)
# плюс количество фактически сбитых кеглей за первый бросок шара в следующем фрейме.
#
# Если фрейм остался открытым, то сумма очков будет равна количеству сбитых кеглей в этом фрейме.
#
# Страйк и спэр в последнем фрейме - по 10 очков.
#
# То есть для игры «Х4/34» сумма очков равна 10+10 + 10+3 + 3+4 = 40,
# а для игры «ХXX347/21» - 10+20 + 10+13 + 10+7 + 3+4 + 10+2 + 3 = 92

# Необходимые изменения сделать во всех модулях. Тесты - дополнить.

# "И да, старые правила должны остаться! для внутреннего рынка..." - уточнил менеджер напоследок.
import argparse
import os
from processing_input_file import Processing, NewProcessing

parser = argparse.ArgumentParser(description='Ping script')

parser.add_argument('--input', action="store", dest='input', help="Enter input file!",
                    default="tournament.txt")
parser.add_argument('--output', action="store", dest='output', help="Enter output file!",
                    default="tournament_result.txt")

args = parser.parse_args('--input tournament.txt --output tour_test.txt'.split())
print(args)
all_path = __file__
name_file = os.path.basename(__file__)
print(all_path, name_file, os.getcwd())  # текущий путь можно получить так

path_dir = all_path[:-len(name_file) - 1]
path_dir = os.path.normpath(path_dir)

path_input_file = os.path.join(path_dir, args.input)
path_output_file = os.path.join(path_dir, args.output)

print("Есть два варианта типов правил!")
print("1) X = 20, \= 15")
print("2) Сложные правила")
N = input()
if N in {"1", "2"}:
    if N == '1':
        Processing(input_file=path_input_file, output_file=path_output_file).run()
    if N == '2':
        NewProcessing(input_file=path_input_file, output_file=path_output_file).run()
#зачёт!