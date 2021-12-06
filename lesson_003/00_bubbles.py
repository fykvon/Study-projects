# -*- coding: utf-8 -*-


import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

point = sd.get_point(300, 300)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius, width=2)


# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет

def bubble(point, step, color):
    radius = 50

    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=color, width=2)  # Добавлен рандомный цвет


point = sd.get_point(300, 300)
bubble(point=point, step=20, color=sd.random_color())

# Нарисовать 10 пузырьков в ряд

for x in range(100, 1100, 100):
    point = sd.get_point(x, 100)
    bubble(point=point, step=5, color=sd.random_color())
# Нарисовать три ряда по 10 пузырьков

for x in range(100, 1100, 100):
    for y in range(100, 301, 100):
        point = sd.get_point(x, y)
        bubble(point=point, step=5, color=sd.random_color())

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами


for _ in range(100):
    point = sd.random_point()
    step = sd.random_number(1, 2)  # Вместо random ставлю sd.random_number. От 1 до 2 что бы видны были кружки.
    bubble(point=point, step=step, color=sd.random_color())

sd.pause()

# зачёт!
