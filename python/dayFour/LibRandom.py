'''
i.learning how to use random class library
ii.basic method: seed(), random()
iii.extend method: 1.random number:
                    randint(a, b), getrandbits(bitnum), uniform(a, b),
                    randrange(a, b, step),
               2.random sequence:
                    choice(), shuffle()

iv.princeple: give a seed -> 梅森旋转算法  // seed --> random
v. capability of using random number
Q: why should we set a seed?
A: 种子提供了随机算法操作的操作数，如果不提供，系统将使用系统时间作为种子，
   这样产生的随机数是不可在线的。



'''

import random as rd


def rdint(a, b):
    rd.seed()
    return int(50 + rd.random() * (b - a))


print("give me a random integer between 50, 100: {}".format(rdint(50, 100)))
