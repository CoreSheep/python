'''
    1.中文词频统计

    jieba three methods need to know
    jieba.lcut(text="text", cut_all=True)       --全模式 lcut is short for list cut
    jieba.lcut(text="text", cut_all=False)      --精确模式
    jieba.lcut_for_search(text="text")          --搜索模式



    2.支持三种分词模式：
    i.精确模式，试图将句子最精确地切开，适合文本分析；
    ii.全模式，把句子中所有的可以成词的词语都扫描出来, 速度非常快，但是不能解决歧义；
    iii.搜索引擎模式，在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词。

'''

import jieba as jb
try:
    txt = open("Threekingdom.txt", 'r', encoding='gbk').read()
except:
    raise FileNotFoundError
else:
    words = jb.lcut(txt)
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
print("{:<10}{:>5}".format("短语", "频率"))
print(items)
for i in range(10):
    word, count = items[i]
    print("{:<10}{:>5}".format(word, count))
