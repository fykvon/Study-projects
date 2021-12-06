#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)

my_family = ['mother', 'father', 'sister']

# список списков приблизителного роста членов вашей семьи

my_family_height = ['Sasha', 164], ['Pasha', 178], ['Dasha', 136]

# ['имя', рост],

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

mother_height = my_family_height[0][1]
father_height = my_family_height[1][1]
sister_height = my_family_height[2][1]

print(' Рост матери  - ', mother_height, ' cm')
print(' Рост отца - ', father_height, ' cm')
print(' Рост сестры - ', sister_height, ' cm')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

sum_height = mother_height + father_height + sister_height
print(' Общий рост моей семьи - ', sum_height, ' cm')
# зачёт!
