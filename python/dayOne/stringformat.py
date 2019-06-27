me = ['SheepCore', 21]
medic = {'name':'SheepCore', 'age':21}

# 1.使用位置参数
print("My name is {} with the age of {}".format("sheepcore".capitalize(), 21))
print("My name is {0} with the age of {1}".format(*me))

# 2.使用关键词参数
print("My name is {name} with the age of {age}".format(name='sheepcore',
                                                       age=21))
print("My name is {name} with the age of {age}".format(**medic))

# 3.填充与格式
# {location : <填充字符><对齐方式><宽度>}
print("{0:*<20}".format("Left Alignment"))
print("{0:*>20}".format("Right Alignment"))
print("{0:*^20}".format("Center Alignment"))



# 4.精度处理
print('{0:.4f}'.format(3.1415))
print('{0:b}'.format(8))
print('{:o}'.format(8))
print('{:x}'.format(32))
print('{:,}'.format(200200200))
