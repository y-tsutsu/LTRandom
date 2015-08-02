# coding: utf-8

import random

with open('LT_list.txt', 'r', encoding = 'shift_jis') as f:
    list = f.readlines()

length = len(list)
if length != 0:
    index = random.randint(0, length - 1)
    print(('最後は ' if length == 1 else '次は ') + list[index][:-1] + ' です(っ´∀｀)っ')
    del list[index]

    with open('LT_list.txt', 'w', encoding = 'shift_jis') as f:
        f.writelines(list)

input('')
