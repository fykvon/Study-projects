# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd
from simple_draw import Point

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

start = sd.get_point(50, 50)
end = sd.get_point(350, 450)

for color in rainbow_colors:
    start.x += 5
    end.x += 5
    sd.line(start_point=start, end_point=end, color=color, width=4)

# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

# Вариант с решением усложнённого задания был ниже. Просто решил сделать несколько вариантов.
# Сейчас убрал все варианты и оставил только самые короткие


# Вариант усложнённого задания с увеличением радиуса


point = sd.get_point(550, 0)
radius = 250

for color in rainbow_colors[::-1]:  # Или так "for color in rainbow_colors:"
    radius += 11
    sd.circle(point, radius=radius, color=color, width=10)
sd.pause()

# зачёт!
