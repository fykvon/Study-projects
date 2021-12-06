# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом


# Вариант через список

long_month = {'1', '3', '5', '7', '8', '10', '12'}
days_in_long_month = 31
short_month = {'4', '6', '9', '11'}
days_in_short_month = 30
february = {'2'}
days_in_february = 28
user_input = input('Please select the month number: ')

if user_input in long_month:
    print(days_in_long_month, 'days in the selected month')
elif user_input in short_month:
    print(days_in_short_month, 'days in the selected month')
elif user_input in february:
    print(days_in_february, 'days in the selected month')
else:
    print('You selected the wrong month number. Please, try again')

# зачёт!
