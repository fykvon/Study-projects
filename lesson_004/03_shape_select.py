# -*- coding: utf-8 -*-

import simple_draw as sd


# Пожалуйста, обратите внимание на перенос строки
# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

def figures(point, angle_quantity, angle):
    step = round(360 / angle_quantity)
    final_angle = 360 - step
    for step in range(angle, final_angle, step):
        point = sd.vector(start=point, angle=step, length=80, width=3)
    sd.line(start_point=point, end_point=point1, width=3)


def triangle(point1, angle):
    figures(point1, angle_quantity=3, angle=angle)


def quad(point1, angle):
    figures(point1, angle_quantity=4, angle=angle)


def pentagon(point1, angle):
    figures(point1, angle_quantity=5, angle=angle)


def hexagon(point1, angle):
    figures(point1, angle_quantity=6, angle=angle)


point1 = sd.get_point(250, 250)
angle = 0
SHAPES = {
    "1": ['triangle', triangle],
    "2": ['quad', quad],
    "3": ['pentagon', pentagon],
    "4": ['hexagon', hexagon]
}

print('Pick a figure')

while True:
    for i in SHAPES:
        print(i, SHAPES[i][0])
    picked_figure = input('pick a number of figure: ')
    if picked_figure in SHAPES:
        draw = SHAPES[picked_figure][1]
        break
    else:
        print('try again')

draw(point1, angle)

sd.pause()

# зачёт!
