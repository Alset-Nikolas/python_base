import unittest
from bowling import GetScore

class ExternalResourceGetterTest(unittest.TestCase):



    def bug_catcher(self, result):
        try:
            A = GetScore(result)
            A.get_score()
        except Exception as err:
            return str(err)


    def test_check_len_long(self):
        err = self.bug_catcher('X'*10)
        Er_expected =str(Exception('Не прошла проверку на корректность данных: не соответствует длина!'))
        self.assertEqual(str(err), Er_expected)

    def test_check_len_short(self):
        err = self.bug_catcher('X'*1)
        Er_expected = str(Exception('Не прошла проверку на корректность данных: не соответствует длина!'))
        self.assertEqual(str(err), Er_expected)

    def test_edge_cases_v1(self):
        err = self.bug_catcher('X//1212')
        Er_expected = str(Exception('Не прошла проверку на корректность данных: inverted spare  !'))
        self.assertEqual(str(err), Er_expected)

    def test_edge_cases_v2(self):
        err = self.bug_catcher('X/11212')
        Er_expected = str(Exception('Не прошла проверку на корректность данных: inverted spare  !'))
        self.assertEqual(str(err), Er_expected)

    def test_summa_nearby_v1(self):
        err = self.bug_catcher('X911212')
        Er_expected = str(Exception(f'Не прошла проверку на корректность данных: mistake summa !'))
        self.assertEqual(str(err), Er_expected)

    def test_all_symbols_v1(self):
        err = self.bug_catcher('X011212')
        Er_expected = str(Exception(f'Не прошла проверку на корректность данных: mistake letter'))
        self.assertEqual(str(err), Er_expected)
    def test_all_symbols_v2(self):
        err = self.bug_catcher('X*11212')
        Er_expected = str(Exception(f'Не прошла проверку на корректность данных: mistake letter'))
        self.assertEqual(str(err), Er_expected)
    def test_all_symbols_v3(self):
        err = self.bug_catcher('X!11212')
        Er_expected = str(Exception(f'Не прошла проверку на корректность данных: mistake letter'))
        self.assertEqual(str(err), Er_expected)

    def test_rus_x(self):
        err = self.bug_catcher('Х!11212')
        Er_expected = str(Exception(f'ввод Х на русском! Требуется X EN'))
        self.assertEqual(str(err), Er_expected)

if __name__ == '__main__':
    # запускам автодискавер тестов
    unittest.main()