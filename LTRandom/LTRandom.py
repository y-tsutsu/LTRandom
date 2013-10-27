# coding: utf-8

import random

f = open("LT_list.txt", "r", encoding = "shift_jis")
list = f.readlines()
f.close()

length = len(list)
if length != 0:
    index = random.randint(0, length - 1)
    print(("最後は " if length == 1 else "次は ") + list[index].replace("\n", "") + " です(っ´∀｀)っ")
    del list[index]

    f = open("LT_list.txt", "w", encoding = "shift_jis")
    f.writelines(list)
    f.close()

input("")
