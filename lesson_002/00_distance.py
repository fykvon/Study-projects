#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


Moscow = sites['Moscow']
London = sites['London']
Paris = sites['Paris']

Moscow_London = ((Moscow[0] - London[0]) ** 2 + (Moscow[1] - London[1]) ** 2) ** 0.5
Moscow_Paris = ((Moscow[0] - Paris[0]) ** 2 + (Moscow[1] - Paris[1]) ** 2) ** 0.5
London_Paris = ((London[0] - Paris[0]) ** 2 + (London[1] - Paris[1]) ** 2) ** 0.5

distances = dict()

distances['Moscow'] = {}
distances['Moscow']['London'] = Moscow_London
distances['Moscow']['Paris'] = Moscow_Paris

distances['London'] = {}
distances['London']['Paris'] = London_Paris
distances['London']['Moscow'] = Moscow_London

distances['Paris'] = {}
distances['Paris']['London'] = London_Paris
distances['Paris']['Moscow'] = Moscow_Paris

from pprint import pprint

pprint(distances)

# Вариант 2

# Тут мы берём именно координаты х и у

x_Moscow = sites.get('Moscow')[0]
y_Moscow = sites.get('Moscow')[1]
x_London = sites.get('London')[0]
y_London = sites.get('London')[1]
x_Paris = sites.get('Paris')[0]
y_Paris = sites.get('Paris')[1]

moscow_london = ((x_Moscow - x_London) ** 2 + (y_Moscow - y_London) ** 2) ** 0.5
moscow_paris = ((x_Moscow - x_Paris) ** 2 + (y_Moscow - y_Paris) ** 2) ** 0.5
london_paris = ((x_London - x_Paris) ** 2 + (y_London - y_Paris) ** 2) ** 0.5

distances = dict()

distances['Moscow'] = {}
distances['Moscow']['London'] = moscow_london
distances['Moscow']['Paris'] = moscow_paris

distances['London'] = {}
distances['London']['Paris'] = london_paris
distances['London']['Moscow'] = moscow_london

distances['Paris'] = {}
distances['Paris']['London'] = london_paris
distances['Paris']['Moscow'] = moscow_paris

from pprint import pprint

pprint(distances)
# первый вариант выглядит проще.
# зачёт!
