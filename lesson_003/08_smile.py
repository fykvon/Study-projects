# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw
import random


# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smile(point):
    x = point.x
    y = point.y
    face = simple_draw.get_point(point.x, point.y)
    radius_face = 50
    eye_f = simple_draw.get_point(-20 + x, 20 + y)
    eye = simple_draw.get_point(20 + x, 20 + y)
    radius_eye = 10
    width = 2
    start_point_line = simple_draw.get_point(-20 + x, -20 + y)
    end_point_line = simple_draw.get_point(20 + x, -20 + y)
    color = simple_draw.COLOR_YELLOW  # Цвет не рандомный, что бы было видно выполнение. Можно simple_draw.random_color()
    # сделать, но они сливаются
    simple_draw.circle(center_position=face, radius=radius_face, color=color, width=width)
    simple_draw.circle(center_position=eye_f, radius=radius_eye, color=color, width=width)
    simple_draw.circle(center_position=eye, radius=radius_eye, color=color, width=width)
    simple_draw.line(start_point=start_point_line, end_point=end_point_line, color=color, width=width)


for y in range(10):
    point = simple_draw.random_point()
    smile(point=point)

simple_draw.pause()

# зачёт!
