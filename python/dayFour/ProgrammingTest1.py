'''
打印所有四位玫瑰数（各个位的四次幂只和等于这个数本身）
'''

def rosenum():
    for i in range(1000, 10000):
        rose = 0
        for c in str(i):
            rose += eval(c) ** 4
        if rose == i:
            print(rose)

rosenum()
