'''
默认参数, 全局变量， 局部变量
'''

s, n = 10, 10
def fact(n, m=1):
    global s
    s = 1
    for i in range(1, n+1):
        s *= i
    return s, s / m, n;

print(fact(10, 10), s, n)