# -*- coding: utf-8 -*-

# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В mastermind_engine нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
#
# В текущем модуле (lesson_006/01_mastermind.py) реализовать логику работы с пользователем:
#   модуль движка загадывает число
#   в цикле, пока число не отгадано
#       у пользователя запрашивается вариант числа
#       проверяем что пользователь ввел допустимое число (4 цифры, все цифры разные, не начинается с 0)
#       модуль движка проверяет число и выдает быков/коров
#       результат быков/коров выводится на консоль
#  когда игрок угадал таки число - показать количество ходов и вопрос "Хотите еще партию?"
#
# При написании кода учитывайте, что движок игры никак не должен взаимодействовать с пользователем.
# Все общение с пользователем (вывод на консоль и запрос ввода от пользователя) делать в 01_mastermind.py.
# Движок игры реализует только саму функциональность игры. Разделяем: mastermind_engine работает
# только с загаданным числом, а 01_mastermind - с пользователем и просто передает числа на проверку движку.
# Это пример применения SOLID принципа (см https://goo.gl/GFMoaI) в архитектуре программ.
# Точнее, в этом случае важен принцип единственной ответственности - https://goo.gl/rYb3hT


import random


def player():

    while True:
        player_number = input('Угадайте число загаданное компьютером ')
        if not player_number.isdigit():
            print('НЕ вводите буквы или знаки! Только цифры!')
        elif int(player_number[0]) == 0:
            print('Не начинай с 0')
        elif 4 < len(set(player_number)) or len(set(player_number)) < 4:
            print('Введите 4 цифры, все цифры разные, не начинается с 0')
        else:
            print('Ваше число принято!')
            return list(int(i) for i in player_number)


def comp():
    global secret_numbers
    secret_numbers = []
    second_part_list = []

    while len(set(secret_numbers)) < 4:
        secret_numbers = [random.randint(1, 9)]
        secret_numbers.extend(second_part_list)

        if len(set(second_part_list)) < 3:
            second_part_list = list(set(second_part_list))
            second_part_list.append(random.randint(0, 9))




def count_bulls_and_cows(player_number):
    global secret_numbers
    cows = 0
    bulls = 0
    for index, player_numeral in enumerate(player_number):
        if player_numeral in secret_numbers:
            if player_numeral == secret_numbers[index]:
                bulls += 1
            else:
                cows += 1

    print("Быков: ", bulls, " Коров: ", str(cows))
    return bulls, cows
