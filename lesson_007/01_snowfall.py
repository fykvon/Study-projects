# -*- coding: utf-8 -*-

import simple_draw as sd
import random


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


#
# class Snowflake:
#
#     def __init__(self):
#         self.x = sd.random_number(0, 600)
#         self.y = 600
#         self.length = sd.random_number(10, 50)
#         self.color=sd.COLOR_WHITE
#
#     def clear_previous_picture(self):
#         point = sd.get_point(self.x, self.y)
#         sd.snowflake(center=point, color=sd.background_color, length=self.length)
#
#     def draw(self):
#         point = sd.get_point(self.x, self.y)
#         sd.snowflake(center=point, color=self.color, length=self.length)
#
#     def move(self):
#         self.y -= 25
#
#     def can_fall(self):
#         return self.y >= 0
#
#
# flake = Snowflake()
#
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
#


# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:


class Snowflake:

    def __init__(self):
        self.x = sd.random_number(0, 600)
        self.y = sd.random_number(600, 800)
        self.length = sd.random_number(10, 50)

    def clear_previous_picture(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, color=sd.background_color, length=self.length)

    def draw(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, color=sd.COLOR_WHITE, length=self.length)

    def move(self):
        self.y -= 15
        random_x = random.randint(-10, 10)
        self.x += random_x

    def can_fall(self):
        return self.y <= 0


def get_flakes(count):
    flakes_list = []
    for _ in range(count):
        flakes_list.append(Snowflake())
    return flakes_list


def get_fallen_flakes():
    global flakes
    fall_list = []  # Возможно лучше переменную счётчик для экономии памяти
    for one_flake in flakes:
        if one_flake.can_fall():
            fall_list.append(one_flake)
            flakes.remove(one_flake)
    return len(fall_list)


def append_flakes(count):
    global flakes
    for _ in range(count):
        flakes.append(Snowflake())
    return flakes


N = 5

flakes = get_flakes(count=N)  # создать список снежинок
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# зачёт!
