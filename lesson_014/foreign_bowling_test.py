# -*- coding: utf-8 -*-

class Bowling:

    def __init__(self, name, game_result):
        self.name = name
        self.game_result = game_result
        self.result = int()
        self.frame_count = 0
        self.throw = 0
        self.throw_number = 0

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

    def foreign_strike_points_counter(self):
        if len(self.game_result) - self.throw_number >= 2:
            next_point = self.game_result[self.throw_number]
            after_next_point = self.game_result[self.throw_number + 1]
            if next_point.isdigit():
                self.result += int(next_point)
            if after_next_point.isdigit():
                self.result += int(after_next_point)
            if next_point == 'X':
                self.result += 10
            if after_next_point == 'X':
                self.result += 10
            if after_next_point == '/':
                self.result -= int(next_point)
                self.result += 10
        else:
            self.foreign_spare_points_counter()

    def foreign_spare_points_counter(self):
        if len(self.game_result) - self.throw_number >= 1:
            next_point = self.game_result[self.throw_number]
            if next_point.isdigit():
                self.result += int(next_point)
            if next_point == 'X':
                self.result += 10

    def first_throw(self, points):
        self.throw_number += 1
        if 'X' == points:
            self.result += 10
            self.foreign_strike_points_counter()
            self.frame_count += 1
            self.throw = 0
        elif points.isdigit():
            self.result += int(points)
        elif points == '-':
            self.result += 0
        else:
            raise Exception('Неверный ввод! Первый бросок в фрейме может быть равен Х,'
                            ' "-" или количество сбитых кеглей')

    def second_throw(self, points, prev_points):
        self.throw_number += 1
        if '/' == points:
            self.result += 10 - int(prev_points)
            self.foreign_spare_points_counter()
            self.frame_count += 1
        elif points.isdigit():
            self.result += int(points)
            if prev_points.isdigit():
                count_frame_points = int(points) + int(prev_points)
                if count_frame_points >= 10:
                    raise Exception(
                        "Результат не должен превышаться 9 баллов за 1 фрейм, если не Х или /")
            self.frame_count += 1
        elif '-' == points:
            self.frame_count += 1

    def run(self):
        self.get_score()
        return self.result
