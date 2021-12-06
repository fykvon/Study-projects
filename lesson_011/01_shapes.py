# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def figures(point, angle, length):
        step = round(360 / n)
        for step in range(angle, 360, step):
            point = sd.vector(start=point, angle=step, length=length, width=3)

    return figures


draw_triangle = get_polygon(n=int(input('Введи количество сторон  ')))
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)

sd.pause()

# зачёт!
