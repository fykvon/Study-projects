# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water:

    def __init__(self):
        self.argument = 'Water'

    def __str__(self):
        return self.argument

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return None


class Air:

    def __init__(self):
        self.argument = 'Air'

    def __str__(self):
        return self.argument

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None


class Fire:

    def __init__(self):
        self.argument = 'Fire'

    def __str__(self):
        return self.argument

    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Earth):
            return Lava()
        else:
            return None


class Earth:

    def __init__(self):
        self.argument = 'Earth'

    def __str__(self):
        return self.argument

    def __add__(self, other):
        if isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Water):
            return Dirt()

        else:
            return None


class Storm:

    def __init__(self):
        self.name = 'Storm'

    def __str__(self):
        return self.name


class Steam:

    def __init__(self):
        self.name = 'Steam'

    def __str__(self):
        return self.name


class Dust:

    def __init__(self):
        self.name = 'Dust'

    def __str__(self):
        return self.name


class Dirt:

    def __init__(self):
        self.name = 'Dirt'

    def __str__(self):
        return self.name


class Lightning:

    def __init__(self):
        self.name = 'Lightning'

    def __str__(self):
        return self.name


class Lava:

    def __init__(self):
        self.name = 'Lava'

    def __str__(self):
        return self.name


print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Fire(), '=', Fire() + Water())
print(Water(), '+', Earth(), '=', Water() + Earth())
print(Fire(), '+', Air(), '=', Fire() + Air())
print(Fire(), '+', Earth(), '=', Fire() + Earth())
print(Air(), '+', Earth(), '=', Earth() + Air())

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.

# зачёт!
