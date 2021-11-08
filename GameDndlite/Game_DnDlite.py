# -*- coding: utf-8 -*-


import json
import re
from decimal import Decimal

field_names = ['current_location', 'current_experience', 'current_date']
find_exp = r'exp\d*'
find_time = r'tm\d*.d*'

with open("rpg.json", "r") as read_file:
    dungeon_data = json.load(read_file)


class Hero:

    def __init__(self, mobs, location):
        self.list_with_available_mobs = mobs
        self.list_with_available_location = location

    def player_choose(self) -> str:
        """Данный метод делает числовой запрос и возвращает выбор пользователя в виде строки"""
        while True:
            if len(self.list_with_available_location) != 0:
                print('-------------------------------------------------\n')
                print('Из этой локации вы можете перeйти в другую локацию')
                print("Для перехода вам доступны локации:\n")
                n = 1
                for location in self.list_with_available_location:
                    print(n, location)
                    n += 1
            if len(self.list_with_available_location) == 0:
                print('Вы в тупике и ждёте своей смерти от наводнения')
                return 'Вы проиграли'
            if len(self.list_with_available_mobs) != 0:
                n = 1
                print('В этой локации вы можете атаковать монстров')
                for mob in self.list_with_available_mobs:
                    print(n, mob)
                    n += 1
            print('\nВыберите действие:\n1.Атаковать монстра\n2.Перейти в другую локацию\n3.Сдаться и выйти из игры')
            try:
                player_choose = input()
                if int(player_choose) == 1:
                    return self.fight_with_mob()
                if int(player_choose) == 2:
                    return self.go_to_next_location()
                if int(player_choose) == 3:
                    return "Вы выбрали сдаться"
            except:
                print('Неверный ввод. Повторите ввод')

    def fight_with_mob(self) -> str:
        """Возвращает выбранного монстра"""
        if self.list_with_available_mobs == []:
            print('В этой локации нет монстров, перейдите в другую')
            return self.player_choose()
        try:
            pick_mob = int(input('Введите номер монстра '))
            mob_name = self.list_with_available_mobs[pick_mob - 1]
            return mob_name
        except:
            print('Неверный ввод. Повторите ввод')
            return self.player_choose()

    def go_to_next_location(self) -> str:
        """Возвращает выбранную локацию"""
        print("Вы выбрали перейти в другую локацию")
        try:
            pick_location = int(input('Введите номер локации\n'))
            location_name = self.list_with_available_location[pick_location - 1]
            return location_name
        except:
            print('Неверный ввод. Повторите ввод')
            return self.player_choose()


class Mobs:
    """Данный класс расчитывает затраченное время на убийство моба, а так же полученный опыт за его убийство"""

    def __init__(self, mob_data):
        self.exp = 0
        self.wasted_time = 0
        self.mob_data = mob_data

    def count_wasted_time_and_exp_in_location(self):
        mobs_time = re.search(find_time, self.mob_data)
        mobs_exp = re.search(find_exp, self.mob_data)
        self.exp = Decimal(mobs_exp.group()[3:])
        self.wasted_time = mobs_time.group()[2:]


class Location:
    """Данный класс расчитывает затраченное время на прохождение локации"""

    def __init__(self, location_name):
        self.name = r'Location_\d*' or r'Hatch_\d*'
        self.location_name = location_name
        self.wasted_time = 0

    def count_wasted_time_in_location(self):
        location_time = re.search(find_time, self.location_name)
        self.wasted_time = location_time.group()[2:]


class Dungeon:
    def __init__(self):
        self.remaining_time = '123456.0987654321'
        self.wasted_time = 0
        self.exp = 0
        self.select_list_location = []
        self.rework_data = []
        self.select_list_mobs = []
        self.json_file = dungeon_data

    def find_location_and_mobs(self, game_steps):
        if isinstance(game_steps, dict):
            for location, info in game_steps.items():
                if 'Hatch' in location:
                    print(info)
                    break
                else:
                    self.select_list_location.append(location)
        if isinstance(game_steps, list):
            for element in game_steps:
                if isinstance(element, dict):
                    for location, info in element.items():
                        self.select_list_location.append(location)
                if isinstance(element, str):
                    self.select_list_mobs.append(element)

    def location_step(self, hero_step):
        try:
            self.json_file = self.json_file[hero_step]
            self.find_location_and_mobs(self.json_file)
            self.select_list_location.remove(hero_step)
        except:
            index = 0
            index = self.select_list_location.index(hero_step) + len(self.select_list_mobs)
            self.json_file = self.json_file[index][hero_step]
            self.select_list_mobs.clear()
            self.select_list_location.clear()
            self.find_location_and_mobs(self.json_file)

    def mob_step(self, hero_step):
        self.json_file.remove(hero_step)
        self.select_list_mobs.remove(hero_step)

    def check_wasted_time_in_location(self, hero_step):
        location = Location(location_name=hero_step)
        location.count_wasted_time_in_location()
        w_time = location.wasted_time
        self.wasted_time += Decimal(w_time)
        if Decimal(self.wasted_time) >= Decimal(123456.0987654321):
            print("У вас кончилось время")
            return

    def hatch(self):
        if self.wasted_time >= Decimal(self.remaining_time):
            print(self.wasted_time)
            print(Decimal(self.remaining_time))
            print("У вас вышло время")
            print('Вы проиграли')
        elif Decimal(self.exp) < 280:
            print(self.exp)
            print("Вам не хватило опыта")
            print('Вы проиграли')
        else:
            print("You are winner")

    def check_wasted_time_mob(self, hero_step):
        mob = Mobs(mob_data=hero_step)
        mob.count_wasted_time_and_exp_in_location()
        w_time = mob.wasted_time
        earn_exp = Decimal(mob.exp)
        self.wasted_time += Decimal(w_time)
        self.exp += Decimal(earn_exp)
        if Decimal(self.wasted_time) >= Decimal(123456.0987654321):
            print('ЗАТРАЧЕННОЕ ВРЕМЯ', self.wasted_time)
            return "У вас кончилось время"

    def main(self):
        print('Вы стоите перед входом в подземелье')
        self.find_location_and_mobs(game_steps=self.json_file)
        hero = Hero(mobs=self.select_list_mobs, location=self.select_list_location)
        while True:
            hero_step = hero.player_choose()
            if 'Вы' in hero_step:
                print(hero_step)
                break
            if 'Location' in hero_step:
                self.location_step(hero_step)
                self.check_wasted_time_in_location(hero_step)
                print('ЗАТРАЧЕННОЕ ВРЕМЯ', self.wasted_time)
                print('НАКОПЛЕННО ОПЫТА', self.exp)
            elif 'Hatch' in hero_step:
                self.hatch()
                break
            elif 'Boss' or 'Mob' in hero_step:
                self.check_wasted_time_mob(hero_step)
                self.mob_step(hero_step)
                print('ЗАТРАЧЕННОЕ ВРЕМЯ', self.wasted_time)
                print('НАКОПЛЕННО ОПЫТА', self.exp)


if __name__ == '__main__':
    game = Dungeon()
    game.main()
