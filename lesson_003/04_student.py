# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

n_procent = 3 / 100  # TODO нейминг! n_procent -> percents_change
kol_vo_mecazev = 10  # TODO нейминг! kol_vo_mecazev -> months

summa = expenses - educational_grant

while kol_vo_mecazev != 0:
    kol_vo_mecazev -= 1
    dif = expenses * (1 + n_procent) - educational_grant
    summa += dif
else:
    print('Студенту надо попросить', round(summa, 2), 'рублей')

# TODO ответ неверный. Подсчёт расходов реализован с ошибкой
