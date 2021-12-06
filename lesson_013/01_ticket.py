# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.pip freeze > requirements.txt
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru


# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.


import argparse
from ticket import TicketFiller as ticket

ticket_01 = argparse.ArgumentParser(description="Let's fill our information in the ticket ")
ticket_01.add_argument('--fio', type=str, help='Input you Name and Surname')
ticket_01.add_argument('--from_', type=str, help='Enter the city of departure')
ticket_01.add_argument('--to', type=str, help='Enter the city of arrival')
ticket_01.add_argument('--date', type=str, help='Enter the date of departure')
args = ticket_01.parse_args()


def main():
    fill_the_ticket = ticket(passanger_name=args.fio, where=args.from_, to=args.to, departure_date=args.date)
    fill_the_ticket.template_maker()


if __name__ == '__main__':
    main()

# def simple_ticket_filler(passanger_name, where, to, departure_date):
#     im = Image.open('images/ticket_template.png')
#     draw = ImageDraw.Draw(im)
#     font = ImageFont.truetype("arial.ttf", size=16)
#     y = 120
#     param_list = [passanger_name, where, to]
#     for i in param_list:
#         draw.text((50, y), i, font=font, fill=ImageColor.colormap['black'])
#         y = y + 70
#     draw.text((280, 260), departure_date, font=font, fill=ImageColor.colormap['black'])
#     im.show()
#
#
# passanger_name = input('Введите ваше ФИО:  ')
# where = input('Откуда вылетаем?  ')
# to = input('Куда летим?  ')
# departure_date = input('Когда прилетаем?  ')
# simple_ticket_filler(passanger_name=passanger_name, where=where, to=to, departure_date=departure_date)

# зачёт!
