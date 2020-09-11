import unittest
from bowling import GetScore

class ExternalResourceGetterTest(unittest.TestCase):



    def bug_catcher(self, result):
        with self.assertRaises(Exception) as cm:
            A = GetScore(result)
            A.get_score()
        return str(cm.exception)

    def test_check_len_long(self):
        some_exception = Exception('Не прошла проверку на корректность данных: не соответствует длина!')
        the_exception =self.bug_catcher('X'*20)
        self.assertEqual(the_exception, str(some_exception))

    def test_check_len_short(self):
        some_exception = Exception('Не прошла проверку на корректность данных: не соответствует длина!')
        the_exception = self.bug_catcher('X' * 1)
        self.assertEqual(the_exception, str(some_exception))

    def test_edge_cases_v1(self):
        some_exception = Exception('Не прошла проверку на корректность данных: inverted spare  !')
        the_exception = self.bug_catcher('X//' + '1'*16)
        self.assertEqual(the_exception, str(some_exception))


    def test_edge_cases_v2(self):
        some_exception = Exception('Не прошла проверку на корректность данных: inverted spare  !')
        the_exception = self.bug_catcher('X/' + '1'*17)
        self.assertEqual(the_exception, str(some_exception))


    def test_summa_nearby_v1(self):
        some_exception = Exception(f'Не прошла проверку на корректность данных: mistake summa !')
        the_exception = self.bug_catcher('X9' + '1'*17)
        self.assertEqual(the_exception, str(some_exception))


    def test_all_symbols_v1(self):
        some_exception = Exception(f'Не прошла проверку на корректность данных: mistake letter')
        the_exception = self.bug_catcher('X0' + '1'*17)
        self.assertEqual(the_exception, str(some_exception))

    def test_all_symbols_v2(self):
        some_exception = Exception(f'Не прошла проверку на корректность данных: mistake letter')
        the_exception = self.bug_catcher('X*' + '1'*17)
        self.assertEqual(the_exception, str(some_exception))

    def test_all_symbols_v3(self):
        some_exception = Exception(f'Не прошла проверку на корректность данных: mistake letter')
        the_exception = self.bug_catcher('X!' + '1'*17)
        self.assertEqual(the_exception, str(some_exception))


    def test_rus_x(self):
        some_exception = Exception(f'ввод Х на русском! Требуется X EN')
        the_exception = self.bug_catcher('Х!' + '1'*17)
        self.assertEqual(the_exception, str(some_exception))



if __name__ == '__main__':
    # запускам автодискавер тестов
    unittest.main()