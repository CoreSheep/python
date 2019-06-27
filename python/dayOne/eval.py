'''
using eval method to drop the outer single or double quote
'''

# 1. 去掉引号成为表达式语句
print(eval("1"))
print(eval("1    /  2"))
eval("print('my name is sheepcore')")

# 2.切片语句  slice format [start : stop : step] 适用于string, list
num = [1, 2, 3, 4, 5]
print(eval("num[:-1]"))


expression = input()
print("{0:.2f}".format(eval(expression)))