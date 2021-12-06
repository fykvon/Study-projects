# -*- coding: utf-8 -*-

import simple_draw as sd
import random

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длин лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20


# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


# snowfall = [[50, 500, sd.random_number(a=10, b=100)], [80, 500, sd.random_number(a=10, b=100)], \
#                       [110, 500, sd.random_number(a=10, b=100)], [140, 500, sd.random_number(a=10, b=100)], \
#                       [170, 500, sd.random_number(a=10, b=100)], [200, 500, sd.random_number(a=10, b=100)], \
#                       [230, 500, sd.random_number(a=10, b=100)], [260, 500, sd.random_number(a=10, b=100)], \
#                       [290, 500, sd.random_number(a=10, b=100)], [320, 500, sd.random_number(a=10, b=100)], \
#                       [350, 500, sd.random_number(a=10, b=100)], [380, 500, sd.random_number(a=10, b=100)], \
#                       [410, 500, sd.random_number(a=10, b=100)], [440, 500, sd.random_number(a=10, b=100)], \
#                       [470, 500, sd.random_number(a=10, b=100)], [500, 500, sd.random_number(a=10, b=100)], \
#                       [530, 500, sd.random_number(a=10, b=100)], [580, 500, sd.random_number(a=10, b=100)], \
#                       [20, 550, sd.random_number(a=10, b=100)], [50, 550, sd.random_number(a=10, b=100)],]

#
# def snow():
#     snowfall = []
#     for i in range(N):
#         snowfall.append([sd.random_number(0, 600), sd.random_number(600, 1200), sd.random_number(10, 100)])
#     while True:
#         sd.clear_screen()
#         for index, (x, y, length) in enumerate(snowfall):
#             point = sd.get_point(x, y)
#             sd.snowflake(center=point, length=length)
#             snowfall[index][1] -= sd.random_number(5, 50)
#             if length > y:
#                 snowfall[index][1] = sd.random_number(600, 1200)
#         sd.sleep(0.1)
#
#         if sd.user_want_exit():
#             break
#
#
# snow()
#
# sd.pause()

# Примерный алгоритм отрисовки снежинок
#   навсегда
#     очистка экрана
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       изменить координата_у и запомнить её в списке по индексу
#       создать точку отрисовки снежинки по координатам
#       нарисовать снежинку белым цветом в этой точке
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл

# зачёт первой части.

# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла: полная очистка всего экрана - долгая операция.
# - использовать хак для стирания старого положения снежинки:
#       отрисуем её заново на старом месте, но цветом фона (sd.background_color) и она исчезнет!
# - использовать функции sd.start_drawing() и sd.finish_drawing()
#       для начала/окончания отрисовки кадра анимации
# - между start_drawing и finish_drawing библиотека sd ничего не выводит на экран,
#       а сохраняет нарисованное в промежуточном буфере, за счет чего достигается ускорение анимации
# - в момент вызова finish_drawing все нарисованное в буфере разом покажется на экране
def snow():
    snowfall = []
    for i in range(N):
        snowfall.append(
            [
                sd.random_number(0, 600),
                sd.random_number(600, 1200),
                sd.random_number(10, 100)]
        )

    while True:
        sd.start_drawing()  # начать рисование кадра
        for index, (x, y, length) in enumerate(snowfall):  # для индекс, координата_х из списка координат снежинок
            point = sd.get_point(x, y)  # создать точку отрисовки снежинки
            sd.snowflake(center=point, color=sd.background_color, length=length)  # нарисовать снежинку цветом фона
            snowfall[index][1] -= sd.random_number(5, 50)  # изменить координата_у и запомнить её в списке по индексу
            new_point = sd.get_point(x, snowfall[index][1])  # создать новую точку отрисовки снежинки
            sd.snowflake(center=new_point, color=sd.COLOR_WHITE, length=length)  # нарисовать снежинку на новом
            # месте белым цветом
            if length > y:
                snowfall[index][1] = sd.random_number(600, 1200)
                sd.snowflake(center=new_point, color=sd.background_color, length=length)  # что бы не было сугроба внизу
                #  Хорошо, рад, что Вы поняли, как сделать усложнённое задание =)
        sd.finish_drawing()  # закончить рисование кадра
        sd.sleep(0.1)

        if sd.user_want_exit():
            break


snow()
sd.pause()

# Примерный алгоритм ускоренной отрисовки снежинок
#   навсегда
#     начать рисование кадра
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     закончить рисование кадра
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

# зачёт!
