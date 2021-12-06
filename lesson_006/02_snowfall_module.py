# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

#  нарисовать_снежинки_цветом(color=sd.background_color)
#  сдвинуть_снежинки()
#  нарисовать_снежинки_цветом(color)
#  если есть номера_достигших_низа_экрана() то
#       удалить_снежинки(номера)
#       создать_снежинки(count)


from snowfall import list_flake, make_flake, step_snowfall, drop_flakes, delete_flake, append

list_flake(10)

while True:
    sd.start_drawing()
    make_flake(color=sd.background_color)
    step_snowfall()
    make_flake()
    dropped_flakes = drop_flakes()
    if dropped_flakes:
        delete_flake(dropped_flakes)
        append(legth_list=len(dropped_flakes))

    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# , восстановил примерный алгорит для отрисовки.
# создать_снежинки(N)
# while True:
#     #  нарисовать_снежинки_цветом(color=sd.background_color)
#     #  сдвинуть_снежинки()
#     #  нарисовать_снежинки_цветом(color)
#     #  если есть номера_достигших_низа_экрана() то
#     #       удалить_снежинки(номера)
#     #       создать_снежинки(count)  # , эта строка отсутствует.
#     # , В неё необходимо передавать количество элементов списка, из списка,
#     # , который возвращает drop_snowflakes().
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
#
# sd.pause()

# зачёт!
