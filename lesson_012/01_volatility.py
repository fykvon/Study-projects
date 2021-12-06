# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от полусуммы крайних значений цены за торговую сессию:
#   полусумма = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / полусумма) * 100%
# Например для бумаги №1:
#   half_sum = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / half_sum) * 100 = 8.7%
# Для бумаги №2:
#   half_sum = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / half_sum) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>


import os
import time


class VolatilityCounter:
    def __init__(self, name):
        self.name = name

    def open_file(self):
        file_open = open(self.name)
        price_list = []
        for line in file_open:
            reworked_line = line.split(',')
            price = reworked_line[2]
            if not price.isalpha():
                price_list.append(price)
        max_price = max(price_list)
        min_price = min(price_list)
        half_sum = (float(max_price) + float(min_price)) / 2
        volatility = ((float(max_price) - float(min_price)) / half_sum) * 100
        tick_name = self.name[14:18]
        return tick_name, round(volatility, 2)


class StatReworker:

    def __init__(self, main_folder_name):
        self.main_folder_name = main_folder_name
        self.files = os.listdir(self.main_folder_name)
        self.zero_vol = []
        self.stat_vol = []

    def get_volatility(self):
        for name_files in self.files:
            single_file_name = VolatilityCounter(os.path.join(self.main_folder_name, name_files))
            run_vol = single_file_name.open_file()
            if run_vol[1] == 0:
                self.zero_vol.append(run_vol[0])
            if run_vol[1] > 0:  # ЛУчше else, в таком случае, если 0, то не будет следующей проверки.
                self.stat_vol.append(run_vol)

    def sort(self):
        sort_stat = sorted(self.stat_vol, key=lambda vol: vol[1])
        print('Максимальная волатильность:')
        for ticker, volatility in sort_stat[:-4:-1]:
            print('{0} : {1} %'.format(ticker, volatility))
        print('Минимальная волатильность:')
        for ticker, volatility in sort_stat[:3]:
            print('{0} : {1} %'.format(ticker, volatility))
        print('Нулевая волатильность:')
        print(', '.join(self.zero_vol))

    def run(self):
        self.get_volatility()
        self.sort()


def main():
    volatility_counter = StatReworker('trades')
    volatility_counter.run()


start_time = time.time()
main()
print("Время работы %s секунд " % (time.time() - start_time))

# Максимальная волатильность:
# SiH9 - 24.39 %
# PDM9 - 23.2 %
# PDH9 - 22.69 %
#
# Минимальная волатильность:
# CHM9 - 0.95 %
# GOG9 - 0.97 %
# RNU9 - 0.98 %
#
# Нулевая волатильность:
# CLM9, CYH9, EDU9, EuH0, EuZ9, JPM9, MTM9, O4H9, PDU9, PTU9, RIH0, RRG9, TRH9, VIH9

# зачёт!
