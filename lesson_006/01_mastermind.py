# -*- coding: utf-8 -*-

# Игра «Быки и коровы»
# https://goo.gl/Go2mb9
#
# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число c неповторяющимися цифрами,
# компьютер сообщают о количестве «быков» и «коров» в названном числе
# «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
#       что и в задуманном числе
# «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
#       что и в задуманном числе
#
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».
#
# Формат ответа компьютера
# > быки - 1, коровы - 1


# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В mastermind_engine нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
#
# В текущем модуле (lesson_006/01_mastermind.py) реализовать логику работы с пользователем:
#   модуль движка загадывает число
#   в цикле, пока число не отгадано
#       у пользователя запрашивается вариант числа
#       проверяем что пользователь ввел допустимое число (4 цифры, все цифры разные, не начинается с 0)
#       модуль движка проверяет число и выдает быков/коров
#       результат быков/коров выводится на консоль
#  когда игрок угадал таки число - показать количество ходов и вопрос "Хотите еще партию?"
#
# При написании кода учитывайте, что движок игры никак не должен взаимодействовать с пользователем.
# Все обще
# ние с пользователем (вывод на консоль и запрос ввода от пользователя) делать в 01_mastermind.py.
# Движок игры реализует только саму функциональность игры. Разделяем: mastermind_engine работает
# только с загаданным числом, а 01_mastermind - с пользователем и просто передает числа на проверку движку.
# Это пример применения SOLID принципа (см https://goo.gl/GFMoaI) в архитектуре программ.
# Точнее, в этом случае важен принцип единственной ответственности - https://goo.gl/rYb3hT

import mastermind_engine as me
from termcolor import cprint, colored
from bot_playing import maybe_the_right_number, game_over_bot


def bulls_cows_print(res):
    print('Быки --> {bulls}, Коровы --> {cows}'.format(bulls=res['bulls'], cows=res['cows']))


exit = False

while not exit:
    cprint('-----Игра «Быки и коровы»-------', color='yellow')
    NUMBER_WIN = me.make_number()
    print('\tМашина загадала число!\n'
          '\t         |\n'
          '\t         |\n'
          '\t         |\n'
          '\t         v\n'
          '\t        ****')
    print('\t\t', NUMBER_WIN)
    number_of_moves = 0

    cprint('------------Кто играет?--------\n', color='yellow')
    cprint('0)------------>Бот', color='yellow')
    cprint('1)------------>Вы\n', color='yellow')
    while True:
        flag = input(colored('-------------->', color='magenta'))
        if flag not in {'0', '1'}:
            cprint('0)------------>Бот', color='yellow')
            cprint('1------------->Вы', color='yellow')
        else:
            cprint('\n------------START---------------', color='yellow')
            break

    if flag == '1':
        while True:

            print()
            number_user = input(
                colored('Введите четырехзначное число c неповторяющимися цифрами!\n\t\t---->', color='magenta'))

            cprint('Ход {}'.format(number_of_moves + 1), color='green')
            number_user = me.check_input(number_user)
            if number_user:
                print('------------------------------')
                print('Ввод: ', number_user)
                print('------------------------------')
                me.checking_number(number_user)

                res = me.checking_number(number_user)

                if res:
                    bulls_cows_print(res)
                    number_of_moves += 1
                    if me.game_over(number_user):
                        cprint('-------!!!WIN!!!-------------', color='red')
                        break
            else:
                print('Некорректный ввод!')

        cprint('Всего на {} ход'.format(number_of_moves), color='green')


    elif flag == '0':

        while True:
            number_bot = maybe_the_right_number()

            cprint('Ход {}'.format(number_of_moves + 1), color='green')
            number_bot = me.check_input(number_bot)
            if number_bot:
                print('------------------------------')
                print('Ввод: ', number_bot)
                print('------------------------------')
                me.checking_number(number_bot)

                res = me.checking_number(number_bot)

                if res:
                    bulls_cows_print(res)
                    number_of_moves += 1
                    if me.game_over(number_bot):
                        cprint('-------!!!WIN!!!-------------', color='red')
                        game_over_bot()
                        break

            else:
                print('Некорректный ввод!')
        cprint('\tВсего на {} ход'.format(number_of_moves), color='red')
    else:
        print('Error!! flag = ', flag)

    cprint('\n------------Еще раз?--------\n', color='yellow')
    cprint('Ввод(Enter)--->Да', color='yellow')
    cprint('Любая)-------->Нет\n', color='yellow')
    exit = input()

# TODO при повторной партии загаданное число остаётся прежним и не генерируется заново
