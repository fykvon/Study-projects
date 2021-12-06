# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

import zipfile


class Counting_letters:

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}
        self.new_list = list()
        self.total_letters_count = 0

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def stat_collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for letter in line:
                    if letter.isalpha():
                        self.total_letters_count += 1
                        if letter in self.stat:
                            self.stat[letter] += 1
                        else:
                            self.stat[letter] = 1

    def title(self):
        print('+---------+----------+\n|{txt: ^9}|'.format(txt='letter') + '{txt: ^10}|\n'.format(
            txt='frequency') + '+---------+----------+')

    def total(self):
        print('+---------+----------+')
        print('|{txt: ^9}|'.format(txt='Total') + '{txt: ^10}|'.format(txt=self.total_letters_count))
        print('+---------+----------+')

    def sorting(self):
        pass

    def prepare_list(self):
        self.new_list = list(self.stat.items())

    def print_statbody(self):
        for letter, count in self.new_list:
            print('|{txt: ^9}|'.format(txt=letter) + '{txt: ^10}|'.format(txt=count))

    def run(self):
        self.unzip()
        self.stat_collect()
        self.title()
        self.prepare_list()
        self.sorting()
        self.print_statbody()
        self.total()


# class Print_stat(Counting_letters):
#     def sorting(self):
#         for letter, count in self.stat.items():
#             print('|{txt: ^9}|'.format(txt=letter) + '{txt: ^10}|'.format(txt=count))


class Sort_A_z(Counting_letters):
    def sorting(self):
        self.new_list.sort()


class Sort_z_A(Counting_letters):
    def sorting(self):
        self.new_list.sort(reverse=True)


class Sort_max_min(Counting_letters):
    def sorting(self):
        self.new_list.sort(key=lambda i: i[1], reverse=True)


if __name__ == '__main__':
    file_name = 'python_snippets/voyna-i-mir.txt.zip'
    # sort = Print_stat(file_name=file_name)  # Общая статистика
    # sort.run()

    sort = Sort_A_z(file_name=file_name)  # Сотировка от А до ё
    sort.run()

    sort = Sort_z_A(file_name=file_name)  # Сотировка от ё до А
    sort.run()
    #
    sort = Sort_max_min(file_name=file_name)  # Сотировка по убыванию
    sort.run()

# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию

# зачёт!
