#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}
from pprint import pprint

# Создайте словарь цен на продкты следующего вида (писать прямо в коде)
sweets = {
    'печенье':
        [
            {'shop': 'ашан', 'price': 10.99},
            {'shop': 'пятерочка', 'price': 9.99},
            {'shop': 'магнит', 'price': 11.99}
        ],
    'конфеты':
        [
            {'shop': 'ашан', 'price': 34.99},
            {'shop': 'пятерочка', 'price': 32.99},
            {'shop': 'магнит', 'price': 30.99}
        ],
    'карамель':
        [
            {'shop': 'ашан', 'price': 45.99},
            {'shop': 'пятерочка', 'price': 46.99},
            {'shop': 'магнит', 'price': 41.99}
        ],
    'пирожное':
        [
            {'shop': 'ашан', 'price': 67.99},
            {'shop': 'пятерочка', 'price': 59.99},
            {'shop': 'магнит', 'price': 62.99}
        ],
    'мороженное':
        [
            {'shop': 'ашан', 'price': 55.99},
            {'shop': 'пятерочка', 'price': 50.99},
            {'shop': 'магнит', 'price': 52.99}
        ],
}
# Указать надо только по 2 магазина с минимальными ценами
#  не до конца понял задание. Полагаю что нужно сделать как сделан вариант ниже?

sweets_min = {
    'печенье':
        [
            {'shop': 'ашан', 'price': 10.99},
            {'shop': 'пятерочка', 'price': 9.99},
        ],
    'конфеты':
        [
            {'shop': 'пятерочка', 'price': 32.99},
            {'shop': 'магнит', 'price': 30.99}
        ],
    'карамель':
        [
            {'shop': 'ашан', 'price': 45.99},
            {'shop': 'магнит', 'price': 41.99}
        ],
    'пирожное':
        [
            {'shop': 'пятерочка', 'price': 59.99},
            {'shop': 'магнит', 'price': 62.99}
        ],
    'мороженное':
        [
            {'shop': 'пятерочка', 'price': 50.99},
            {'shop': 'магнит', 'price': 52.99}
        ],
}

pprint(sweets_min)

# зачёт!
