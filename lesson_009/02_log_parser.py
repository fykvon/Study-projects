# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

class Log_parser:

    def __init__(self, name):
        self.name = name
        self.time_in_line = None
        self.min = None
        self.new_dict = dict()
        self.cut = None

    def open_file(self):
        with open(self.name, 'r', encoding='cp1251') as file:
            self.minute(file)

    def minute(self, file):
        total = 0
        for line in file:
            self.min = line[:self.cut]
            if 'NOK' in line:
                if self.time_in_line == self.min:
                    total += 1
                else:
                    if total != 0:
                        self.new_dict[self.time_in_line] = total
                    total = 1
                    self.time_in_line = self.min
        self.new_dict[self.time_in_line] = total

    def prepare(self):
        for key, value in self.new_dict.items():
            with open('new_file.txt', 'a', encoding='cp1251') as new_file:
                new_file.write(f' {key}]:{value}\n')

    def sorting(self):
        pass

    def act(self):
        self.sorting()
        self.open_file()
        self.prepare()


class Sort_minute(Log_parser):
    def sorting(self):
        self.cut = 17


class Sort_month(Log_parser):
    def sorting(self):
        self.cut = 8


class Sort_year(Log_parser):
    def sorting(self):
        self.cut = 5


class Sort_hour(Log_parser):
    def sorting(self):
        self.cut = 14


if __name__ == '__main__':
    name = 'events.txt'
    # sort = Sort_year(name=name)
    # sort.act()
    sort = Sort_hour(name=name)
    sort.act()
    # sort = Sort_month(name=name)
    # sort.act()
    # sort = Sort_year(name=name)
    # sort.act()

# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году

# зачёт!
