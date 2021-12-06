# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall
#

snowfall = []


def list_flake(N):
    global snowfall

    for i in range(N):
        snowfall.append(
            [
                sd.random_number(0, 600),
                sd.random_number(600, 600),
                sd.random_number(10, 100)])


def make_flake(color=sd.COLOR_WHITE):
    global snowfall
    for index, (x, y, length) in enumerate(snowfall):
        point = sd.get_point(x, y)
        sd.snowflake(center=point, color=color, length=length)


def step_snowfall():
    global snowfall
    for index, flake in enumerate(snowfall):
        flake[1] -= sd.random_number(5, 50)


def drop_flakes():
    global snowfall
    coord_drop = []
    for (x, y, length) in snowfall:
        if y < -50:
            coord_drop.append([x, y, length])
    return coord_drop


def delete_flake(coord_drop):
    global snowfall
    for i in coord_drop:
        snowfall.remove(i)


def append(legth_list):
    global snowfall
    for _ in range(legth_list):
        snowfall.append(
            [
                sd.random_number(0, 600),
                sd.random_number(600, 600),
                sd.random_number(10, 100)])
