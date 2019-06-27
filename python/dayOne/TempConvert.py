'''
python 语法分析
1.缩进，注释，命名，变量，保留字
2.数据类型，整型，浮点型，字符串类型，列表类型，字典，元组
3.赋值语句，分支语句，函数
'''

TempStr = input("please input a temperature with the 'F' or 'C' attched to "
                "the end\n")
if TempStr[0] in ['F', 'f']:
    C = (eval(TempStr[1:]) - 32) / 1.8
    print("After converting: {:.2f}C".format(C))
elif TempStr[0] in ['C', 'c']:
    F = 1.8 * eval(TempStr[1:]) + 32
    print("After converting: {:.2f}F".format(F))
else:
    print("Wrong input format, please check it out.")


