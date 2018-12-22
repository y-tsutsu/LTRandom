import random

with open('lt_list.txt', 'r', encoding='utf-8') as f:
    file = f.readlines()

if file != []:
    choice = random.choice(file)
    print(('最後は ' if len(file) == 1 else '次は ') + choice[:-1] + ' です(っ´∀｀)っ')
    file.remove(choice)

    with open('lt_list.txt', 'w', encoding='utf-8') as f:
        f.writelines(file)
