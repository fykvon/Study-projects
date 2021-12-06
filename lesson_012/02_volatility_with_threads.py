# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
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
import os
import threading
import time


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)\n')
        return result

    return surrogate


class VolatilityCounter(threading.Thread):
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.tick_name = self.name[14:18]
        self.volatility = int()

    def run(self):
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
        self.volatility = round(volatility, 2)
        return self.volatility


class StatReworker:

    def __init__(self, main_folder_name):
        self.path = main_folder_name
        self.zero_vol = []
        self.stat_vol = {}

    @time_track
    def get_volatility(self):
        files = os.listdir(self.path)
        full_path_list = []
        for ifile in files:
            full_path_list.append(os.path.join(self.path, ifile))
        multy = [VolatilityCounter(path) for path in full_path_list]
        for one in multy:
            one.start()
            # print(one.ident) ID потоков разные)
        for one in multy:
            one.join()
        for one in multy:
            if one.volatility == 0:
                self.zero_vol.append(one.tick_name)
            elif one.volatility > 0:
                self.stat_vol[one.tick_name] = one.volatility

    def sort(self):
        sort_stat = sorted(self.stat_vol.items(), key=lambda vol: vol[1])
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
    stat_rew = StatReworker('trades')
    stat_rew.run()


if __name__ == '__main__':
    main()

# зачёт!
