# -*- coding: utf-8 -*-
from typing import Union, Tuple

import simple_draw as sd


# Пожалуйста, обратите внимание на перенос текста.


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

def figures(point, color, angle_quantity, angle, length):
    step = round(360 / angle_quantity)
    final_angle = 360 - step
    for step in range(angle, final_angle, step):
        point = sd.vector(start=point, angle=step, length=length, color=color, width=3)
    sd.line(start_point=point, end_point=point1, color=color1, width=3)


def triangle(point1, color, angle, length):
    figures(point=point1, color=color, angle_quantity=3, angle=angle, length=length)


def quad(point1, color, angle, length):
    figures(point=point1, color=color, angle_quantity=4, angle=angle, length=length)


def pentagon(point1, color, angle, length):
    figures(point=point1, color=color, angle_quantity=5, angle=angle, length=length)


def hexagon(point1, color, angle, length):
    figures(point=point1, color=color, angle_quantity=6, angle=angle, length=length)


COLORS = {"1": ['RED', sd.COLOR_RED],
          "2": ['ORANGE', sd.COLOR_ORANGE],
          "3": ['YELLOW', sd.COLOR_YELLOW],
          "4": ['GREEN', sd.COLOR_GREEN],
          "5": ['CYAN', sd.COLOR_CYAN],
          "6": ['BLUE', sd.COLOR_BLUE],
          "7": ['PURPLE', sd.COLOR_PURPLE]}

print('Color list:')

while True:
    for i in COLORS:
        print(i, COLORS[i][0])
    color_check = input('select number color ')
    if color_check in COLORS:
        color1 = COLORS[color_check][1]
        break
    else:
        print('try again')

point1 = sd.get_point(100, 100)
triangle(point1, color=color1, angle=0, length=80)
point1 = sd.get_point(300, 100)
quad(point1, color=color1, angle=0, length=80)
point1 = sd.get_point(300, 300)
pentagon(point1, color=color1, angle=0, length=80)
point1 = sd.get_point(100, 300)
hexagon(point1, color=color1, angle=0, length=80)

sd.pause()

# зачёт!
