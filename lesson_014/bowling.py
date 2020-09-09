def show(game_result):
    '''
    Вывод на  экран
    '''
    print('----------------------')
    len_i = 0
    print('Ввод:')
    for letter in game_result:

        if letter == 'X':
            print('X', end='')
            len_i += 2
        else:
            print(letter, end='')
            len_i += 1
        if len_i % 2 == 0:
            print(' ', end='')
    print('\n----------------------')


def check_len(game_result, number_of_frames):
    '''
    Проверяем длину
    '''
    if game_result.count('X') + len(game_result) != 2 * number_of_frames:
        print(game_result.count('X') + len(game_result))

        raise Exception('Не прошла проверку на корректность данных: не соответствует длина!')


def check_edge_cases(game_result):
    '''
    Возможные проблемы с /
    '''
    len_i = 0
    for letter in game_result:
        if letter == 'X':
            len_i += 2
        else:
            len_i += 1
        if len_i % 2 == 1 and letter == '/':
            raise Exception('Не прошла проверку на корректность данных: inverted spare  !')


def check_summa_nearby(game_result):
    '''
        Возможные проблемы с суммой в каждом из фреймов
    '''
    i = 0
    while i < len(game_result) - 1:

        if game_result[i].isdigit() and game_result[i + 1].isdigit():
            if int(game_result[i]) + int(game_result[i + 1]) > 10:
                raise Exception(f'Не прошла проверку на корректность данных: mistake summa  '
                                f'{game_result[i]}+{game_result[i + 1]}>10 !')
            i += 1
        i += 1


def check_all_symbols(game_result):
    all_symbols = {'X', "/", '-'} | {str(x) for x in range(10)}
    for letter in game_result:
        if letter not in all_symbols:
            raise Exception(f'Не прошла проверку на корректность данных: mistake letter', letter)

def check_param(game_result):
    '''
    Проверка на корректность данных  Например:«Х4/34-4»
    '''
    number_of_frames = 4
    check_len(game_result, number_of_frames)
    check_all_symbols(game_result)
    check_edge_cases(game_result)
    check_summa_nearby(game_result)



def get_score(game_result):
    show(game_result)
    check_param(game_result)
    result = 0
    i = 0
    while i < len(game_result) - 1:
        if game_result[i] =='X':
            result +=20
            i-=1
        elif game_result[i].isdigit() and game_result[i + 1].isdigit():
            result += int(game_result[i]) + int(game_result[i + 1])
        elif game_result[i + 1] == '/':
            result +=15
        elif game_result[i] == '-' and game_result[i + 1].isdigit():
            result +=int(game_result[i + 1])
        elif game_result[i+1] == '-' and game_result[i].isdigit():
            result += int(game_result[i])
        i+=2
    return result

get_score('X4/14-4')
