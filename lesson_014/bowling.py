# -*- coding: utf-8 -*-

from collections import Counter
import logging

# пожалуйста, обратите внимание, параметр handlers должен принимать на вход словарь типа
# 'default': {
#     'level': 'INFO',
#     'formatter': 'standard',
#     'class': 'logging.StreamHandler',
#     'stream': 'ext://sys.stdout',
# },
logging.basicConfig(level=logging.INFO, handlers=[logging.FileHandler('tournament_errors.log', 'w', 'utf-8')])


class Bowling:

    def __init__(self, file_name, output):
        self.file_name = file_name
        self.result = int()
        self.frame_count = 0
        self.throw = 0
        self.throw_number = 0
        self.tour_dict = {}
        self.output = output
        self.tour_dict_full = {}
        self.player_name_result_dict = {}
        self.reworked_line = None
        self.winners_list = []
        self.for_print = []

    def open_file(self):  # тут создаётся словарь словарей.
        with open(file=self.file_name, mode='r', encoding='utf-8') as file:
            for line in file:
                self.reworked_line = line.split()

                if 'Tour' in self.reworked_line:
                    tour_number = self.reworked_line[1] + ' ' + self.reworked_line[2]
                    self.tour_dict[tour_number] = {}
                self.round_counter(self.reworked_line, tour_number)
                self.winner_found(self.reworked_line, tour_number)

    def round_counter(self, reworked_line, tour_number):

        if len(reworked_line) == 2:
            player_name = reworked_line[0]
            result = reworked_line[1]
            prev_points = 0
            self.frame_count = 0
            self.result = 0
            self.throw_number = 0
            self.for_print.append(player_name)
            try:
                self.frames(result=result, prev_points=prev_points)
            except Exception as err:
                logging.error(f'{tour_number} {player_name} {err}')
                self.throw = 0
            else:
                self.player_name_result_dict[player_name] = [result, self.result]

    def winner_found(self, reworked_line, tour_number):
        if 'winner' in reworked_line:
            try:
                if len(self.player_name_result_dict) == 0:
                    raise Exception()
            except:
                logging.info(f'{tour_number} Winner did not find. All results was incorrect')
            else:
                self.tour_dict_full.update({tour_number: self.player_name_result_dict})  # добавляем словарь
                # словарей за тур

            self.tour_dict = {}
            self.player_name_result_dict = {}

    def frames(self, result, prev_points):  # тут происходит подсчёт результатов за 1 раунд 1 игрока
        for points in result:
            self.throw += 1
            if self.throw == 1:
                self.first_throw(points)
            elif self.throw == 2:
                self.second_throw(points, prev_points)
                self.throw = 0
            if self.frame_count > 10:
                raise Exception(f'{self.frame_count} Максимальное число фреймов не более 10')
            prev_points = points

    def sort_tour_dict(self):
        new_list = []

        with open(file=self.output, mode='a', encoding='utf-8') as output_file:
            for tour, information in self.tour_dict_full.items():
                output_file.write(f'{tour}\n')
                for name, value in information.items():
                    result = value[0]
                    points = value[1]

                    output_file.write(f'{name} {result} {points}\n')
                    new_list.append([name, result, points])
                    new_list.sort(key=lambda i: i[2], reverse=True)
                self.winners_list.append(new_list[0][0])
                output_file.write(f'winner is {new_list[0][0]}\n\n')
                new_list = []

    def output_resutlt(self):

        count_how_much_games_was_played = Counter(self.for_print)
        count_winners = Counter(self.winners_list)
        print('+----------+------------------+--------------+')
        print('|   Игрок  |  сыграно матчей  |  всего побед |')
        print('+----------+------------------+--------------+')
        for winners_name, winner in count_winners.items():
            for name, games in count_how_much_games_was_played.items():
                if winners_name == name:
                    print('|{txt: ^10}|'.format(txt=name) + '{txt: ^18}|'.format(txt=games) +
                          '{txt: ^14}|'.format(txt=winner))
        print('+----------+------------------+--------------+')

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
                    raise Exception(
                        "Результат не должен превышаться 9 баллов за 1 фрейм, если не Х или /")
            self.frame_count += 1
        elif '-' == points:
            self.frame_count += 1

    def run(self):
        self.open_file()
        self.sort_tour_dict()
        self.output_resutlt()


class BowlingForForeign(Bowling):

    def foreign_strike_points_counter(self):
        if len(self.reworked_line[1]) - self.throw_number >= 2:
            next_point = self.reworked_line[1][self.throw_number]
            after_next_point = self.reworked_line[1][self.throw_number + 1]
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
        if len(self.reworked_line[1]) - self.throw_number >= 1:
            next_point = self.reworked_line[1][self.throw_number]
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

# Bowling(file_name='tournament.txt', output='result.txt').run()
