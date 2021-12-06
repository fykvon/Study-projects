# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def opener(line):
    legth_list = list(line.split(' '))
    if len(legth_list) < 3:
        raise ValueError('Не верные данные')
    name, email, age = line.split(' ')
    if '@' not in email and '.' not in email:
        raise NotEmailError('Ошибка в email')
    elif not name.isalpha():
        raise NotNameError('Ошибка в имени')
    elif 10 >= int(age):
        raise ValueError('Возраст выходит за рамки')
    elif int(age) >= 99:
        raise ValueError('Возраст выходит за рамки')


with open('registrations.txt', 'r', encoding='utf-8') as ff:
    for line_number, line in enumerate(ff):
        try:
            opener(line)
            with open('registrations_good.log.txt', 'a', encoding='utf-8') as bad_good:
                bad_good.write(f'{line}')
        except (ValueError, NotEmailError, NotNameError) as error:
            with open('registrations_bad.log.txt', 'a', encoding='utf-8') as bad_log:
                bad_log.write(f'Ошибка в линии номер {line_number + 1} {line} {error}\n')

# зачёт!
