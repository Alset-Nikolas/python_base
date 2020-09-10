class GetScore:

    def __init__(self, game_result, number_of_frames=4):
        self.game_result = game_result
        self.number_of_frames = number_of_frames

    def check_len(self):
        '''
        Проверяем длину
        '''
        if self.game_result == '':
            raise Exception('Не прошла проверку на корректность данных: длина!')
        if self.game_result.count('X') + len(self.game_result) != 2 * self.number_of_frames:
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
    A = GetScore('X4/14-4')
    print(A.get_score())
