import random

with open('lt_list.txt', 'r', encoding='shift_jis') as f:
    file = f.readlines()

if file != []:
    choice = random.choice(file)
    print(('最後は ' if len(file) == 1 else '次は ') + choice[:-1] + ' です(っ´∀｀)っ')
    file.remove(choice)

    with open('lt_list.txt', 'w', encoding='shift_jis') as f:
        f.writelines(file)
