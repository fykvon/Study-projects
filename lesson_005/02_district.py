# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join


from district.central_street.house1.room1 import folks as c_h1_r_1
from district.central_street.house1.room2 import folks as c_h1_r_2
from district.central_street.house2.room1 import folks as c_h2_r_1
from district.central_street.house2.room2 import folks as c_h2_r_2
from district.soviet_street.house1.room1 import folks as s_h1_r_1
from district.soviet_street.house1.room2 import folks as s_h1_r_2
from district.soviet_street.house2.room1 import folks as s_h2_r_1
from district.soviet_street.house2.room2 import folks as s_h2_r_2
from pprint import pprint

folk = []
# ЛУчше не нагромождать =)
folk.extend(c_h1_r_1)
folk.extend(c_h1_r_2)
folk.extend(c_h2_r_1)
folk.extend(c_h2_r_2)
folk.extend(s_h1_r_1)
folk.extend(s_h1_r_2)
folk.extend(s_h2_r_1)
folk.extend(s_h2_r_2)

print('На районе живут:')
pprint(', '.join(folk))

# зачёт!
