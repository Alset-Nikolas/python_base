#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
#----------------------------------Лампа-------------------------------------------------------
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price

print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')


# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

#----------------------------------Стол---------------------------------------------------------

stol_code = goods['Стол']
stol_item_0 = store[stol_code][0]
stol_item_0_quantity = stol_item_0['quantity']
stol_item_0_price = stol_item_0['price'] * stol_item_0_quantity
stol_item_1 = store[stol_code][1]
stol_item_1_quantity = stol_item_1['quantity']
stol_item_1_price = stol_item_1['price'] * stol_item_1_quantity
stol_quantity = stol_item_0_quantity + stol_item_1_quantity
stol_cost = stol_item_0_price + stol_item_1_price
print('Стол -', stol_quantity, 'шт, стоимость', stol_cost, 'руб')

#----------------------------------Диван---------------------------------------------------------
divan_code = goods['Диван']
divan_item_0 = store[divan_code][0]
divan_item_0_quantity = divan_item_0['quantity']
divan_item_0_price = divan_item_0['price'] * divan_item_0_quantity
divan_item_1 = store[divan_code][1]
divan_item_1_quantity = divan_item_1['quantity']
divan_item_1_price = divan_item_1['price'] * divan_item_1_quantity
divan_quantity = divan_item_0_quantity + divan_item_1_quantity
divan_cost = divan_item_0_price + divan_item_1_price
print('Диван -', divan_quantity, 'шт, стоимость', divan_cost, 'руб')
#----------------------------------Стул---------------------------------------------------------
stul_code = goods['Стул']
stul_item_0 = store[stul_code][0]
stul_item_0_quantity = stul_item_0['quantity']
stul_item_0_price = stul_item_0['price'] * stul_item_0_quantity
stul_item_1 = store[stul_code][1]
stul_item_1_quantity = stul_item_1['quantity']
stul_item_1_price = stul_item_1['price'] * stul_item_1_quantity
stul_item_2 = store[stul_code][2]
stul_item_2_quantity = stul_item_2['quantity']
stul_item_2_price = stul_item_2['price'] * stul_item_2_quantity
stul_quantity = stul_item_0_quantity + stul_item_1_quantity + stul_item_2_quantity
stul_cost = stul_item_0_price + stul_item_1_price + stul_item_2_price
print('Стул -', stul_quantity, 'шт, стоимость', stul_cost, 'руб')

# зачёт! 🚀

# --------------------------ВОПРОСИК---------------------------

'''  

Я не понял как исправлялть какой-то коммит http://joxi.ru/eAO85pKCpX53Vr
делаю задание 1,2,3.....11 и для каждого делаю коммит, начал проверять и понимаю, что ошибка есть, например в 3
А как в этом коммте исправить  (что-то дописать или удалить)?

Я понимаю,как исправить последний (Amend Commit) , но чтобы исправить 3, он добавляет это испраление (3-его) в конец

Да, самый не первый коммит изменить можно. Как это делается описано здесь: https://habr.com/ru/post/201922
'''
