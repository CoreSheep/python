'''
sorted and list.sorted
1.内置函数 sorted 是对副本进行排序
2.列表排序是对本身排序
两者参数相同
sorted(iterable, key=None, reverse=False)
'''

#1. list.sort()
num = {'one': 1, 'two': 3, 'three': 2}
print(num.items())
ls = list(num.items())
print(ls)

ls.sort(key=lambda x: x[1], reverse=False)

print(ls)


#2. builtins sorted()
num['four'] = 0
ls = list(num.items())
ls1 = sorted(ls, key=lambda y:y[0], reverse=True )
print(ls1)

ls2 = sorted(ls, key=lambda x:x[1], reverse=False)
print(ls2)
