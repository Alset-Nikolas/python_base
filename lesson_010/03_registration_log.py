# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля+
# - поле имени содержит только буквы+
# - поле емейл содержит @ и .+
# - поле возраст является числом от 10 до 99+
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.
class NotNameError(Exception):
    pass

class NotEmailError(Exception):
    pass


class ParsRegistrationLog:

    def __init__(self, name_file, name_registration_bad_file, name_registration_good_file):
        self.name_file = name_file
        self.name_registration_bad_file = name_registration_bad_file
        self.name_registration_good_file = name_registration_good_file

    def check_email(self,email):
        if '@' in email and '.' in email:
            return True
        return False

    def check_old(self,old):
        if 9 < int(old) < 100:
            return True
        return False


    def pars_line(self,line):
        line_mass = line.split()
        if len(line_mass) == 3:
            [name_user, email_user, old_user] = line_mass
            if not name_user.isalpha():
                raise NotNameError('поле имени содержит НЕ только буквы')

            if not self.check_email(email_user):
                raise NotEmailError('поле емейл НЕ содержит @ или .(точку)')

            if not (old_user.isdigit() and self.check_old(old_user)):
                raise ValueError('поле возраст НЕ является числом от 10 до 99')

        else:
            raise ValueError('НЕ присутсвуют все три поля')

    def main(self):
        with open(self.name_file, encoding='utf-8') as file:
            for line in file:
                line = line[:-1]
                try:
                    self.pars_line(line)
                    with open(self.name_registration_good_file, mode='a', encoding='utf-8') as file:
                        file.write(line+'\n')
                    continue
                except ValueError as arg:
                    print(line, arg)
                except NotNameError as arg:
                    print(line, arg)
                except NotEmailError as arg:
                    print(line, arg)
                with open(self.name_registration_bad_file, mode='a', encoding='utf-8') as file:
                    file.write(line + '\n')


A = ParsRegistrationLog(name_file='registrations.txt',
                        name_registration_bad_file='registrations_bad.log',
                        name_registration_good_file='registrations_good.log')

A.main()