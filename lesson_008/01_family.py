# -*- coding: utf-8 -*-

# from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class Human:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = None

    def get_home(self, house):
        self.house = house

    def get_home_for_cat(self, cat):
        cat.house = self.house
        print('{} купил кота, принёс домой и назвал {}'.format(self.name, cat.name))

    def palm_the_cat(self):
        self.happiness += 5
        self.fullness -= 10
        print('{} гладит котов'.format(self.name))

    def eat(self):
        if self.house.meal_in_freeze < 30:
            print('{} увидел что нет еды в холодильнике'.format(self.name))
            self.fullness -= 10
        else:
            print('{} поел'.format(self.name))
            self.house.meal_in_freeze -= 30
            self.fullness += 30

    def act(self):
        if self.happiness >= 100:
            self.happiness = 100
        if self.fullness <= 0:
            print('{} умер'.format(self.name))
            return False  # если человек умер, то передаётся False
        elif self.happiness < 10:
            print('{} умер'.format(self.name))
            return False  # если человек умер, то передаётся False
        else:  # если человек не умер, то проверяем на грязь и уменьшаем счастье если грязи больше 90. Ну и возвращаем True
            if self.house.dirt >= 90:
                self.happiness -= 10
            return True


class House:

    def __init__(self):
        self.money_in_nightstand = 100
        self.meal_in_freeze = 50
        self.dirt = 0
        self.cat_food = 30

    def __str__(self):
        return 'осталось {} денег, {} еды, {} кошачей еды, {} грязь'.format(self.money_in_nightstand,
                                                                            self.meal_in_freeze, self.cat_food,
                                                                            self.dirt)

    def act(self):
        self.dirt += 5


class Husband(Human):
    count_money = 0
    count_meal = 30

    def __str__(self):
        return '{} сытость {} счастье {}'.format(self.name, self.fullness, self.happiness)

    def act(self):
        if super().act():
            dice = randint(1, 6)  # Тут если в супере True, то действия выполняются, иначе просто пишется name умер.
            if self.fullness < 30:
                self.eat()
                self.count_meal += 30
            elif self.house.money_in_nightstand <= 350:  # Денег 350 что бы не умерла от депрессии жена.(могла купить шубу)
                self.work()
            elif self.happiness < 30:  # что бы не умер от депрессии муж
                if dice == 1:
                    self.palm_the_cat()
                else:
                    self.gaming()
            elif dice == 2:  # рандомные действия
                self.eat()
            elif dice == 4 or 5:  # рандомные действия
                self.work()
            elif dice == 1 or 3:
                self.palm_the_cat()

    def work(self):
        self.house.money_in_nightstand += 150
        self.fullness -= 10
        Husband.count_money += 30
        print('{} усердно работал (деньги + 150)'.format(self.name))

    def gaming(self):
        self.happiness += 20
        self.fullness -= 10
        print('{} играл в WoT'.format(self.name))


class Wife(Human):
    count_fur = 0
    count_meal = 0

    def __str__(self):
        return '{} сытость {} счастье {}'.format(self.name, self.fullness, self.happiness)

    def act(self):
        if super().act():
            dice = randint(1, 6)
            if self.fullness < 40:  # Что бы не умерла от голода
                self.eat()
                self.count_meal += 30
            elif self.house.meal_in_freeze <= 60 or self.house.cat_food <= 20:  # Если нет еды в холодильнике, значит и есть нечего
                self.shopping()
            elif self.house.dirt >= 100:  # моет дом, что бы не было грязно и не падало счастье
                self.clean_house()
            elif self.happiness <= 30:
                if self.house.money_in_nightstand > 350:
                    self.buy_fur_coat()
                else:
                    self.palm_the_cat()
            elif dice == 1:  # рандомные действия
                self.eat()
            elif dice == 4:  # рандомные действие
                self.palm_the_cat()

    def shopping(self):
        if self.house.money_in_nightstand >= 60:
            self.house.meal_in_freeze += 60
            self.fullness -= 10
            if self.house.cat_food >= 100:
                self.house.cat_food += 0
                self.house.money_in_nightstand -= 60
                print('{} Пошла на шопинг (Деньги - 30)'.format(self.name))
            else:
                self.house.cat_food += 20
                self.house.money_in_nightstand -= 80
                print('{} Пошла на шопинг (Деньги - 50)'.format(self.name))
        else:
            print('{} не хватило денег на еду'.format(self.name))

    def buy_fur_coat(self):
        if self.house.money_in_nightstand >= 350:
            self.happiness = +60
            self.fullness -= 10
            Wife.count_fur += 1
            print('{} радовалась новой шубе (Деньги - 350. Счастье +60)'.format(self.name))
        else:
            print('{} не хватило денег на шубу'.format(self.name))

    def clean_house(self):
        self.house.dirt -= 100
        self.fullness -= 10
        if self.house.dirt <= 0:  # Дома не может быть чище чистого.
            self.house.dirt = 0
        print('{} убиралась дома '.format(self.name))


#  после реализации первой части - отдать на проверку учителю
# зачёт первой части.
######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов

class Cat:
    count_food = 0

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.house = None

    def __str__(self):
        return '{} сытость {}'.format(self.name, self.fullness)

    def dead_or_alive(self):
        if self.fullness <= 0:
            return False
        else:
            return True

    def act(self):
        dice = randint(1, 3)
        if self.dead_or_alive() == True:  # Если умер. Значит не выполняем ничего.
            if self.fullness <= 10:
                self.eat()
            elif dice == 1:
                self.sleep()
            elif dice == 2:
                self.soil()
            elif dice == 3:
                self.eat()
        elif self.dead_or_alive() == False:  # если умер, то принтуем.
            print('Кот {} умер'.format(self.name))

    def eat(self):
        if self.house.cat_food <= 0:
            print('Кот {} остался голодным'.format(self.name))
            self.fullness -= 10
        else:
            self.house.cat_food -= 10
            self.fullness += 20
            self.count_food += 10
            print('Кот {} поел'.format(self.name))

    def sleep(self):
        print('Кот {} спал'.format(self.name))
        self.fullness -= 10

    def soil(self):
        print('Кот {} драл обои'.format(self.name))
        self.house.dirt += 5
        self.fullness -= 10


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child(Human):
    count_food = 0

    def __str__(self):
        return '{} сытость {}'.format(self.name, self.fullness, self.happiness)

    def act(self):
        self.happiness = 100
        super().act()
        if super().act() == True:
            if self.fullness <= 20:
                self.eat()
            else:
                self.sleep()

    def eat(self):
        if self.house.meal_in_freeze <= 0:
            print('В холодильнике нет еды')
        else:
            self.fullness += 10
            self.count_food += 10
            print('{} поел'.format(self.name))

    def sleep(self):
        self.fullness -= 10
        print('{} спал'.format(self.name))


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
child = Child(name='Ребёнок')
cat_1 = Cat(name='Кусака')

masha.get_home(house=home)
serge.get_home(house=home)
child.get_home(house=home)
serge.get_home_for_cat(cat=cat_1)

for day in range(365):
    print('================== День {} =================='.format(day))
    serge.act()
    masha.act()
    home.act()
    child.act()
    cat_1.act()

    print(serge)
    print(masha)
    print(child)
    print(cat_1)
    print(home)

print('===============  Итоги за год  =====================')
print('За год {} и {} съели -'.format(serge.name, masha.name), serge.count_meal + masha.count_meal, 'еды')
print('За год Кот {} съел {} еды'.format(cat_1.name, cat_1.count_food))
print('За год {} съел {} еды'.format(child.name, child.count_food))
print('За год {} заработал -'.format(serge.name), serge.count_money, 'денег')
print('За год {} купила -'.format(masha.name), masha.count_fur, 'шуб')

#  после реализации второй части - отдать на проверку учителем две ветки

# зачёт части с ребёнком.
######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

# зачёт!
