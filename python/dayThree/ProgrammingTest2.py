'''
test 2
字符串分段组合
描述
获得输入的一个字符串s，以字符减号(-)分割s，将其中首尾两段用加号(+)组合后输出。
'''

str1 = input()
strsplit = str1.split('-')

print(strsplit[0] + '+' + strsplit[-1])