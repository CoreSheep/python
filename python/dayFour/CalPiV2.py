'''
way of thinking -- 蒙特卡罗撒点法
1. 数学思维： 找到公式，利用公式求解
2. 计算思维： 抽象一种过程，用计算机自动化求解

'''

from random import random
from time import perf_counter

Darts = 3000 * 1000
hits = 0.0
start = perf_counter()

for i in range(0, Darts):
    x, y = random(), random()
    dist = pow(x ** 2 + y ** 2, 0.5)
    if dist <= 1.0:
        hits += 1.0

pi = (hits / Darts) * 4
print("Pi :{:.6f}".format(pi))
print("Time consuming: {:.1f}".format(perf_counter() - start))