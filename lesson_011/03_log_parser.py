# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>  # Итератор или генератор? выбирайте что вам более понятно
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

# class Log_parser:
#
#     def __init__(self, name):
#         self.name = name
#         self.time_in_line = None
#         self.min = None
#         self.open_file = open(self.name, 'r', encoding='cp1251')
#         self.cut = 17
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         total = 0
#         lines = self.open_file.readline()
#         if lines:
#             contain_line = lines[1:17]
#             if 'NOK' in lines:
#                 if self.min == contain_line:
#                     total += 1
#                 else:
#                     total = 1
#                     self.min = contain_line
#             return contain_line, total
#         raise StopIteration
#
#
# grouped_events = Log_parser(name='events.txt')
#
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')

def logger(name):
    open_file = open(name, 'r', encoding='cp1251')
    total = 0
    min = None
    for line in open_file:
        cut_line = line[1:17]
        if 'NOK' in line:
            if min == cut_line:
                total += 1
            else:
                if total != 0:
                    yield min, total
                total = 1
                min = cut_line
    yield min, total


grouped_events = logger(name='events.txt')

for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')

# зачёт!
