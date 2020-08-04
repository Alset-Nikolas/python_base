# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input('Введите, пожалуйста, номер месяца: ')

months = {1: ['Январе', 31],
          2: ['Феврале', 28],
          3: ['Марте', 31],
          4: ['Апреле', 30],
          5: ['Мае', 31],
          6: ['Июне', 30],
          7: ['Июле', 31],
          8: ['Августе', 31],
          9: ['Сентябре', 30],
          10: ['Октябре', 31],
          11: ['Ноябре', 30],
          12: ['Декабре', 31]}

while not user_input:
    print('Вы ничего не ввели! ', end=' ')
    user_input = input('Введите, пожалуйста, номер месяца: ')
else:
    month_probe = float(user_input)
    if month_probe % 10 != 0:
        print('Вы ввели', month_probe)
        print('Предполагалось натуральное число!')
    else:
        month = int(user_input)
        print('Вы ввели', month)
        if 0 < month < 13:
            print('В', months[month][0], ' всего ', months[month][1], ' дней')
        elif month > 12:
            print('Всего 12 месяцев!')
        elif month <= 0:
            print('Предполагалось натуральное число!')
        else:
            print('Что-то случилось!')
