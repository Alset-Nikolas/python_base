class GetScore:

    def __init__(self, game_result, number_of_frames=10):
        self.game_result = game_result
        self.number_of_frames = number_of_frames

    def check_len(self):
        '''
        Проверяем длину
        '''
        if self.game_result == '':
            raise Exception('Не прошла проверку на корректность данных: длина!')
        if self.game_result.count('X') + len(self.game_result) != 2*self.number_of_frames:
            raise Exception('Не прошла проверку на корректность данных: не соответствует длина!')

    def check_edge_cases(self):
        '''
        Возможные проблемы с /
        '''
        len_i = 0
        for letter in self.game_result:
            if letter == 'X':
                len_i += 2
            else:
                len_i += 1
            if len_i % 2 == 1 and letter == '/':
                raise Exception('Не прошла проверку на корректность данных: inverted spare  !')

    def check_summa_nearby(self):
        '''
            Возможные проблемы с суммой в каждом из фреймов
        '''
        i = 0
        while i < len(self.game_result) - 1:

            if self.game_result[i].isdigit() and self.game_result[i + 1].isdigit():
                if int(self.game_result[i]) + int(self.game_result[i + 1]) > 9:
                    raise Exception(f'Не прошла проверку на корректность данных: mistake summa !')
                i += 1
            i += 1

    def check_all_symbols(self):
        all_symbols = {'X', "/", '-'} | {str(x) for x in range(1,10)}
        for letter in self.game_result:
            if letter not in all_symbols:
                raise Exception(f'Не прошла проверку на корректность данных: mistake letter')

    def check_rus_x(self):
        if 'х' in self.game_result or 'Х' in self.game_result:
            raise Exception(f'ввод Х на русском! Требуется X EN')

    def check_param(self):
        '''
        Проверка на корректность данных  Например:«Х4/34-4»
        '''
        self.check_rus_x()
        self.check_len()
        self.check_all_symbols()
        self.check_edge_cases()
        self.check_summa_nearby()

    def get_score(self):
        self.check_param()
        result = 0
        i = 0
        while i < len(self.game_result) - 1:
            if self.game_result[i] == 'X':
                result += 20
                i -= 1
            elif self.game_result[i].isdigit() and self.game_result[i + 1].isdigit():
                result += int(self.game_result[i]) + int(self.game_result[i + 1])
            elif self.game_result[i + 1] == '/':
                result += 15
            elif self.game_result[i] == '-' and self.game_result[i + 1].isdigit():
                result += int(self.game_result[i + 1])
            elif self.game_result[i + 1] == '-' and self.game_result[i].isdigit():
                result += int(self.game_result[i])
            i += 2
        return result


if __name__ == '__main__':
    A = GetScore('--8-X3/4/1/-12651X')
    print(A.get_score())
# TODO Добавлю пару примеров(из следующей части) для того, чтобы вы могли откалибровать ваш алгоритм
# ### Tour 1
# Антон	1/6/1/--327-18812382     Недопустимая комбинация фрейма - «82»
# Елена	3532X332/3/62--62X       105  TODO Вот тут у вас выдаётся неверный ответ
# Роман	725518X--8/--543152      Недопустимая комбинация фрейма - «55»
# Татьяна	8/--35-47/371/518-4/     Недопустимая комбинация фрейма - «37»
# Ринат	4-3/7/3/8/X711627-5      113
# winner is Ринат
#
# ### Tour 2
# Татьяна	42X--3/4/2-8271171/      Недопустимая комбинация фрейма - «82»
# Роман	811/X--3/XX171/43        129
# Ринат	-263X815/5/27-----6      85
# Алексей	--8-X3/4/1/-12651X       108  TODO А вот здесь ошибка, хотя строка верная и должна быть равна 108
# Павел	3-6/5/9/5---1/--5-52     80
# winner is Роман