# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

# Вот такое решение.


for row, y in enumerate(range(0, 1001, 50)):
    # if row % 2 == 0:
    #    a = 0
    # else:
    #     a = 50
    start = 50 if row % 2 else 0  # Удобно! Спасибо за подсказку. Можно стену поставлю так? что бы основание было ровное

    for x in range(start, 1001, 100):
        start = simple_draw.get_point(x, y)
        end = simple_draw.get_point(x + 100, y + 50)
        simple_draw.rectangle(right_top=end, left_bottom=start, color=simple_draw.COLOR_ORANGE, width=1)

simple_draw.pause()
# Сейчас всё правильно =)
# зачёт!
