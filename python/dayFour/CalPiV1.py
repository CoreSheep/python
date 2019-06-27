'''
calculate the value of pi
'''


def calPI(n):
    pi = 0
    for i in range(n):
        pi += (1 / 16 ** i) * (
                    4 / (8 * i + 1) - 2 / (8 * i + 4) -  \
                    1 / (8 * i + 5) - 1 / (8 * i + 6)  \
                    )
    return pi


cyclenum = eval(input("loop times: "))  # 输入是数字，一定进行去引号处理
print("Pi: {}".format(calPI(cyclenum)))
