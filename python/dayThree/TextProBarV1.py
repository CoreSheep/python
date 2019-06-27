'''
text process bar
'''

print("{:-^20}".format("start"))
for i in range(11):
    star = '*' * i
    bar = '-' * (10 - i)
    pronum = i * 10
    print("{: ^3} % [{:}->{:}]".format(pronum, star, bar))
print("{:-^20}".format("end"))

