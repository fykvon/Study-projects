# -*- coding: utf-8 -*-

import simple_draw as sd


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Примерный алгоритм внутри функции:
#   # будем рисовать с помощью векторов, каждый следующий - из конечной точки предыдущего
#   текущая_точка = начальная точка
#   для угол_наклона из диапазона от 0 до 360 с шагом XXX
#      # XXX подбирается индивидуально для каждой фигуры
#      составляем вектор из текущая_точка заданной длины с наклоном в угол_наклона
#      рисуем вектор
#      текущая_точка = конечной точке вектора
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# # sd.get_vector()
# # sd.line()
# # Результат решения см lesson_004/results/exercise_01_shapes.jpg
#
#
# def triangle(point1, angle1=0, length=80):
#     angle_quantity = 3
#     v1 = sd.get_vector(start_point=point1, angle=angle1, length=length, width=3)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle1 + 360 / angle_quantity, length=length, width=3)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle1 + 360 / angle_quantity * 2, length=length, width=3)
#     v3.draw()
#
#
# def quad(point1, angle1=0, length=80):
#     angle_quantity = 4
#     v1 = sd.get_vector(start_point=point1, angle=angle1, length=length, width=3)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle1 + 360 / angle_quantity, length=length, width=3)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle1 + 360 / angle_quantity * 2, length=length, width=3)
#     v3.draw()
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle1 + 360 / angle_quantity * 3, length=length, width=3)
#     v4.draw()
#
#
# def pentagon(point1, angle1=0, length=80):
#     angle_quantity = 5
#     v1 = sd.get_vector(start_point=point1, angle=angle1, length=length, width=3)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle1 + 360 / angle_quantity, length=length, width=3)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle1 + 360 / angle_quantity * 2, length=length, width=3)
#     v3.draw()
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle1 + 360 / angle_quantity * 3, length=length, width=3)
#     v4.draw()
#     sd.line(start_point=v4.end_point, end_point=v1.start_point, width=3)
#
#
# def hexagon(point1, angle1=0, length=80):
#     angle_quantity = 6
#     v1 = sd.get_vector(start_point=point1, angle=angle1, length=length, width=3)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle1 + 360 / angle_quantity, length=length, width=3)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle1 + 360 / angle_quantity * 2, length=length, width=3)
#     v3.draw()
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle1 + 360 / angle_quantity * 3, length=length, width=3)
#     v4.draw()
#     v5 = sd.get_vector(start_point=v4.end_point, angle=angle1 + 360 / angle_quantity * 4, length=length, width=3)
#     v5.draw()
#     sd.line(start_point=v5.end_point, end_point=v1.start_point, width=3)
#
#
# # Илья, пожалуйста, обратите внимание, сначала создаём функции, потом пишем остальной код и вызываем функции.
# point1 = sd.get_point(100, 100)
# triangle(point1=point1, angle1=0, length=80)
# point1 = sd.get_point(300, 100)
# quad(point1=point1, angle1=0, length=80)
# point1 = sd.get_point(300, 300)
# pentagon(point1=point1, angle1=0, length=80)
# point1 = sd.get_point(100, 300)
# hexagon(point1=point1, angle1=0, length=80)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.


# зачёт первой части, пожалуйста, приступайте ко второй

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


#  Также перенесите расчёт текущего угла в range: укажите ему стартовый угол, конечный (с учётом того, чтобы рисовалось
#  на одну сторону меньше) и шаг угла.
def figures(point, angle_quantity, angle, length):
    step = round(360 / angle_quantity)
    final_angle = 360 - step
    for step in range(angle, final_angle, step):
        point = sd.vector(start=point, angle=step, length=length, width=3)
    sd.line(start_point=point1, end_point=point, width=3)


# Если правильно понял задание, то вот так это должно выглядить. Как я понял, мы теперь с помощью  этих функций можем
# вызывать только 1 объект на основе количества углов!

def triangle(point1, angle, length):
    figures(point=point1, angle_quantity=3, angle=angle, length=length)


def quad(point1, angle, length):
    figures(point=point1, angle_quantity=4, angle=angle, length=length)


def pentagon(point1, angle, length):
    figures(point=point1, angle_quantity=5, angle=angle, length=length)


def hexagon(point1, angle, length):
    figures(point=point1, angle_quantity=6, angle=angle, length=length)


# Илья, пожалуйста, обратите внимание, сначала создаём функции и только потом их вызываем и пишем остальной код.

point1 = sd.get_point(100, 100)
triangle(point1=point1, angle=0, length=80)

point1 = sd.get_point(300, 100)
quad(point1, angle=0, length=80)

point1 = sd.get_point(300, 300)
pentagon(point1, angle=0, length=80)

point1 = sd.get_point(100, 300)
hexagon(point1, angle=0, length=80)

# point1 = sd.get_point(300, 100)
# figures(point=point1, angle_quantity=4, angle=0, length=80)
# point1 = sd.get_point(300, 300)
# figures(point=point1, angle_quantity=5, angle=0, length=80)
# point1 = sd.get_point(100, 300)
# figures(point=point1, angle_quantity=6, angle=0, length=80)

sd.pause()

# зачёт!
