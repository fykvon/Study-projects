# -*- coding: utf-8 -*-
import random
from random import choice

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

ENLIGHTENMENT_CARMA_LEVEL = 777


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


def carma_counter():  # По заданию необходимо создать 1 функцию, которая будет и райзить ошибку и возвращать
    # карму? что то это не понял. Эта функция возвращаяет сейчас рандомное значение кармы
    carma = random.randint(1, 7)
    return carma


def one_day():  # Эта функция возвращает ошибку
    seq = [IamGodError('IamGodError'), DrunkError('DrunkError'), CarCrashError('CarCrashError'),
           GluttonyError('GluttonyError'), DepressionError('DepressionError'), SuicideError('SuicideError')]
    random_exception = choice(seq)
    return random_exception


carma = 0

while True:
    carma += carma_counter()
    try:
        raise one_day()
    except (IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError) as error:
        with open('log_день_сурка.log.txt', 'a', encoding='utf-8') as bad_good:
            bad_good.write(f'Ошибка  {error} карма {carma} \n')
    if carma >= ENLIGHTENMENT_CARMA_LEVEL:
        print(f'ЕЕЕЕЕ новый день настал! Ты смог накопить карму до {carma}. Странно что карма растёт от смертей...')
        break

# https://goo.gl/JnsDqu

# зачёт!
