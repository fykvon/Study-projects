# -*- coding: utf-8 -*-

# Прибежал менеджер и сказал что нужно срочно изменить правила подсчета очков в игре.
# "Выходим на внешний рынок, а там правила игры другие!" - сказал он.
#
# Правила подсчета очков изменяются так:
#
# Если во фрейме страйк, сумма очков за этот фрейм будет равна количеству сбитых кеглей в этом фрейме (10 кеглей)
# плюс количество фактически сбитых кеглей за два следующих броска шара (в одном или двух фреймах,
# в зависимости от того, был ли страйк в следующем броске).
# Например: первый бросок шара после страйка - тоже страйк, то +10 (сбил 10 кеглей)
# и второй бросок шара - сбил 2 кегли (не страйк, не важно как закончится этот фрейм - считаем кегли) - то еще +2.
#
# Если во фрейме сбит спэр, то сумма очков будет равна количеству сбитых кеглей в этом фрейме (10 кеглей)
# плюс количество фактически сбитых кеглей за первый бросок шара в следующем фрейме.
#
# Если фрейм остался открытым, то сумма очков будет равна количеству сбитых кеглей в этом фрейме.
#
# Страйк и спэр в последнем фрейме - по 10 очков.
#
# То есть для игры «Х4/34» сумма очков равна 10+10 + 10+3 + 3+4 = 40,
# а для игры «ХXX347/21» - 10+20 + 10+13 + 10+7 + 3+4 + 10+2 + 3 = 92

# Необходимые изменения сделать во всех модулях. Тесты - дополнить.

# "И да, старые правила должны остаться! для внутреннего рынка..." - уточнил менеджер напоследок.

from bowling import Bowling as local_bowling
from bowling import BowlingForForeign as foreign_bowling
import argparse

game = argparse.ArgumentParser(description="This scrip helps you to find a winner in file with game stats")
game.add_argument('--input', help='Enter name input file')
game.add_argument('--output', help='Enter name output file')
game.add_argument('--region', help='Select region (Local or Foreign)')

args = game.parse_args()


def main():
    if args.region == 'Local':
        print('This is local version result')
        local_game = local_bowling(file_name=args.input, output=args.output)
        local_game.run()
    elif args.region == 'Foreign':
        print('This is foreign version result')
        point_count = foreign_bowling(file_name=args.input, output=args.output)
        point_count.run()
    else:
        print('Wrong choose!')


if __name__ == '__main__':
    main()

# зачёт!
