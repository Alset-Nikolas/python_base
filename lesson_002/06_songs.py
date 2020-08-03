#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут

violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],  #
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],  #
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],  #
]

# Распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
# Три песни звучат ХХХ.XX минут
# Точность указывается в функции round(a, b)
# где a, это число которое надо округлить, а b количество знаков после запятой
# более подробно про функцию round смотрите в документации https://docs.python.org/3/search.html?q=round


sum_time = violator_songs[3][1] + violator_songs[-4][1] + violator_songs[-1][1]
sum_time = round(sum_time, 2)  # 14.93 минуты —---> 15.33 минуты
norm_sum_time = 15.33
text_violator_songs = 'Три песни звучат ' + str(norm_sum_time) + ' минут.'
print(text_violator_songs)

# Есть словарь песен группы Yellow со временем звучания с точностью до долей минут
pocket_universe_songs = {
    'Solar Driftwood': 1.85,
    'Celsius': 5.98,
    'More': 6.65,
    'On Track': 5.55,
    'Monolith': 6.35,
    'To the Sea': 5.77,
    'Magnetic': 5.88,
    'Liquid Mountain': 2.97,
    'Pan Blue': 5.52,
    'Resistor': 7.22,
    'Beyond Mirrors': 5.82,
}

# Распечатайте общее время звучания трех песен: 'On Track', 'To the Sea' и 'Beyond Mirrors'
# А другие три песни звучат приблизительно ХХХ минут

time_On_Track = pocket_universe_songs['On Track']
time_To_the_Sea = pocket_universe_songs['To the Sea']
time_Beyond_Mirrors = pocket_universe_songs['Beyond Mirrors']
sum_time_2 = time_On_Track + time_To_the_Sea + time_Beyond_Mirrors
sum_time_2 = round(sum_time_2)


print('А другие три песни звучат приблизительно ' + str(sum_time_2) + ' минут.')

# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

# зачёт! 🚀
