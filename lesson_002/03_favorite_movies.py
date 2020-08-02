#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
# первый фильм
# последний
# второй
# второй с конца


# Запятая не должна выводиться. Переопределять my_favorite_movies нельзя
# Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!


print(my_favorite_movies[:len('Терминатор')])
print(my_favorite_movies[-len('Назад в будущее'):])
print(my_favorite_movies[len("Терминатор, "):len('Терминатор, Пятый элемент')])
print(my_favorite_movies[-len('Чужие, Назад в будущее'):-len(', Назад в будущее')])

''' Если нельзя использовать функцию len(), то вот:
print()
print(my_favorite_movies[:10])
print(my_favorite_movies[-15:])
print(my_favorite_movies[12:25])
print(my_favorite_movies[-22:-17])
'''