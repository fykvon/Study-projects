# -*- coding: utf-8 -*-

class Bowling:

    def __init__(self, name, game_result):
        # def __init__(self, game_result):
        self.name = name
        self.game_result = game_result
        self.result = int()
        self.frame_count = 0
        self.throw = 0

    def get_score(self):
        prev_points = 0
        for points in self.game_result:
            self.throw += 1
            if self.throw == 1:
                self.first_throw(points)
            elif self.throw == 2:
                self.second_throw(points, prev_points)
                self.throw = 0

            if self.frame_count > 10:
                raise Exception('Максимальное число фреймов не более 10')
            prev_points = points

    def first_throw(self, points):
        if 'X' == points:
            self.result += 20
            self.frame_count += 1
            self.throw = 0
        elif points.isdigit():
            self.result += int(points)
        elif '-' == points:
            self.result += 0
        else:
            raise Exception(
                'Неверный ввод! Первый бросок в фрейме может быть равен Х, "-" или количество сбитых кеглей')

    def second_throw(self, points, prev_points):
        if '/' == points:
            self.result += 15 - int(prev_points)
            self.frame_count += 1
        elif points.isdigit():
            self.result += int(points)
            if prev_points.isdigit():
                count_frame_points = int(points) + int(prev_points)
                if count_frame_points >= 10:
                    raise Exception("Результат не должен превышаться 9 баллов за 1 фрейм, если не Х или /")
            self.frame_count += 1
        elif '-' == points:
            self.frame_count += 1

    def run(self):
        self.get_score()
        # print(f'Количество очков для результатов {self.game_result} - {self.result}')
        return self.result

# a = Bowling(name='fdsf',game_result='6353--4428--1/5443--')
# a.run()
# print(a.result)
# print('Ошибочные фреймы:')
# error_list = [
#     '1/6/1/--327-18812382',  # => Недопустимая комбинация фрейма - «82»
#     '725518X--8/--543152',  # => Недопустимая комбинация фрейма - «55»
#     '8/--35-47/371/518-4/',  # Недопустимая комбинация фрейма - «37»
#     '42X--3/4/2-8271171/',  # => Недопустимая комбинация фрейма - «82»
#     '--/5X4/26X4572/2-6',  # Некорректно указан формат => /5
#     '369/8/----4/2/2/-32/XX',  # Некорректное количество фреймов.
#     '--9/5/--42--339//-X',  # Некорректно указан формат => /-!
# ]
# #
# for throw in error_list:
#     try:
#         Bowling(throw).run()
#     except Exception as exc:
#         print(f'Не прошёл: {exc.args}')
#
# print('\nКорректные фреймы:')
# normal_list = [
#     '24X4/626/-41/618-3/',  # 113
#     '4-3/7/3/8/X711627-5',  # 113
#     '3532X332/3/62--62X',  # 105
#     '811/X--3/XX171/43',  # 129
#     '-263X815/5/27-----6',  # 85
#     '--8-X3/4/1/-12651X',  # 108
#     '3-6/5/9/5---1/--5-52',  # 80
# ]
# #
# for throw in normal_list:
#     try:
#         Bowling(throw).run()
#     except Exception as exc:
#         print(f'Не прошёл: {exc.args}')
