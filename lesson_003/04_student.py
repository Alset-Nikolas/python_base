# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

percents_change = 3 / 100

scholarship_for_10_month = 10 * educational_grant
expenses_for_i_month = 0
for _ in range(10):
    expenses_for_i_month += expenses
    expenses *= 1 + percents_change
else:
    print('Студенту надо попросить', round(expenses_for_i_month - scholarship_for_10_month, 2), 'рублей')

'''
#----------------------------------------------------------------------------------------------------------------------

educational_grant, expenses = 10000, 12000
percents_change = 3 / 100
summa = expenses - educational_grant

for _ in range(9):
    expenses *= 1 + percents_change
    summa += expenses - educational_grant

else:
    print('Студенту надо попросить', round(summa, 2), 'рублей')
'''




