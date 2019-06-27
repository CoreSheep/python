'''
    # 统计 Halmet 单词种类和单词出现频率 #
    1. 对文件进行处理
    2. 处理文本文件

    步骤：
        1.open halmet.txt
        2.split txt into list
        3.count the frequency of each word
        4.sorted the list

'''



def getText():
    txt = open("Hamelt.txt", 'r').read()
    txt = txt.lower()
    for c in '~!@#$%^&*()+-={}|[]\:";<>?,./':
        txt = txt.replace(c, ' ')
    return txt

HalmetTxt = getText()
words = HalmetTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
    # counts.get(keyword='word', defaultvalue=0) return 0 if not find such key
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)

for i in range(20):
    (word, count) = items[i]
    print("{0:<10}{1:>5}".format(*(word.capitalize(), count)))
