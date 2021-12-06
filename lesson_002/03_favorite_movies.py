#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
# Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!

# Вариант 1 c помощью среза

print(my_favorite_movies[0:10])  # А ещё, тут можно так my_favorite_movies[:10]
print(my_favorite_movies[42:57])  # А ещё, тут можно так my_favorite_movies[42:]
print(my_favorite_movies[12:25])
print(my_favorite_movies[35:40])

# Вариант 2 создание списка

my_movie_list = ['Терминатор', 'Пятый элемент', 'Аватар', 'Чужие', 'Назад в будущее']
print(my_movie_list[0])
print(my_movie_list[-1])
print(my_movie_list[1])
print(my_movie_list[-2])

# зачёт!
