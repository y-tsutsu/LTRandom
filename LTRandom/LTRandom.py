import codecs
import random

uf = codecs.open("LT_list.txt", "r", "shift-jis")
list = uf.readlines()
uf.close()

length = len(list)
if length != 0:
    index = random.randint(0, length - 1)
    print((u"最後は " if length == 1 else u"次は ") + list[index].replace(u"\r\n", u"") + u" です(っ´∀｀)っ")
    del list[index]

    uf = codecs.open("LT_list.txt", "w", "shift-jis")
    uf.writelines(list)
    uf.close()

raw_input("")
