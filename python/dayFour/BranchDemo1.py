'''
分支语句
'''

# test 1 紧凑二分支结构 一行代码表示分支结构
guess = eval(input())
print("猜{:}了".format("对" if guess==99 else "错"))

# test 2 多分枝结构
grade = eval(input())

if(grade < 60):
    print("E")
elif(grade < 70):
    print("D")
elif(grade < 80):
    print("C")
elif(grade < 90):
    print("B")
else:
    print("A")