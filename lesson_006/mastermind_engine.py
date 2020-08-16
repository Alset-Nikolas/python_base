from random import randint
from termcolor import cprint, colored

NUMBER_WIN = [None] * 4


def game_over(number_user=None):
    '''Конец игры!'''
    if number_user == NUMBER_WIN:
        cprint('-------!!!WIN!!!-------------', color='red')
        exit()
    return False


def make_number():
    ''' Выдает 4-ч значное число, в которм не повторяются числа! '''

    global NUMBER_WIN

    while len(NUMBER_WIN) != len(set(NUMBER_WIN)):
        NUMBER_WIN = [randint(1, 9), randint(0, 9), randint(0, 9), randint(0, 9)]

    print('\tМашина загадала число!\n'
          '\t         |\n'
          '\t         |\n'
          '\t         |\n'
          '\t         v\n'
          '\t        ****')
    print('\t\t', NUMBER_WIN)
    return NUMBER_WIN


def check_input(number_user):
    '''Проверка числа,которое ввел пользователь!'''
    if number_user.isdigit() and len(number_user) == len(set(number_user)) == 4:
        if number_user[0] == '0':
            print('Первый элемент не может быть 0!')
            return False
        else:
            number_user = [int(number_user[0]), int(number_user[1]), int(number_user[2]), int(number_user[3])]
            print('------------------------------')
            print('Ввод: ', number_user)
            print('------------------------------')
            return number_user
    else:
        print('Некорректный ввод!')
        return False


def bulls_cows_print(res):
    print('Быки --> {bulls}, Коровы --> {cows}'.format(bulls=res['bulls'], cows=res['cows']))


def checking_number(number_user):
    ''' Возвращает словарь {'bulls': N, 'cows': N}!'''
    number_user = check_input(number_user)
    if number_user:
        res = {'bulls': 0, 'cows': 0}
        for i in range(len(NUMBER_WIN)):
            if number_user[i] == NUMBER_WIN[i]:
                res['bulls'] += 1

            elif number_user[i] in set(NUMBER_WIN):
                res['cows'] += 1
        game_over(number_user)
        bulls_cows_print(res)
        return res
    else:
        return False


if __name__ == '__main__':
    print(make_number())
    checking_number('1234')

# TODO в mastermind_engine.py никаких сообщений пользователю выводить нельзя.
#  Представьте, что движок работает в паре в веб сайтом - у вебсайта консоли нет!
#  Все общение с пользователем должно быть в вызывающем движок коде (то есть 01_mastermind.py)
