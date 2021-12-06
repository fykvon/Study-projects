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


# СТОЛЫ
table_code = goods['Стол']

table_item_one = store[table_code][0]
table_item_second = store[table_code][1]

# общее кол-во столов
table_quantity = table_item_one['quantity'] + table_item_second['quantity']

# стоимость столов у каждого поставщика
table_first_supplier = table_item_one['quantity'] * table_item_one['price']
table_second_supplier = table_item_second['quantity'] * table_item_second['price']

# общая стоимость всех столов
table_cost = table_first_supplier + table_second_supplier

print('Стол -', table_quantity, 'шт, стоимость', table_cost, 'руб')

# ДИВАНЫ
sofa_code = goods['Диван']
sofa_item_one = store[sofa_code][0]
sofa_item_second = store[sofa_code][1]

# общее кол-во столов
sofa_quantity = sofa_item_one['quantity'] + sofa_item_second['quantity']

# стоимость столов у каждого поставщика
sofa_first_supplier = sofa_item_one['quantity'] * sofa_item_one['price']
sofa_second_supplier = sofa_item_second['quantity'] * sofa_item_second['price']

# общая стоимость всех столов
sofa_cost = sofa_first_supplier + sofa_second_supplier

print('Диван -', sofa_quantity, 'шт, стоимость', sofa_cost, 'руб')

# СТУЛЬЯ
chair_code = goods['Стул']
chair_item_one = store[chair_code][0]
chair_item_second = store[chair_code][1]
chair_item_third = store[chair_code][2]

# считаю общее кол-во стульев
chair_quantity = chair_item_one['quantity'] + chair_item_second['quantity'] + chair_item_third['quantity']

# стоимость стульев у каждого поставщика
chair_first_supplier = chair_item_one['quantity'] * chair_item_one['price']
chair_second_supplier = chair_item_second['quantity'] * chair_item_second['price']
chair_third_supplier = chair_item_third['quantity'] * chair_item_third['price']

# общая стоимость всех стульев
chair_cost = chair_first_supplier + chair_second_supplier + chair_third_supplier

print('Стул -', chair_quantity, 'шт, стоимость', chair_cost, 'руб')

##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################
# Молодец, что пишите комментарии =)
# зачёт!
