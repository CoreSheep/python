'''
using Lambda Expression to simplify the process of defining a method
anonymous method
'''

def add(x, y):
    return x + y

plus = lambda x, y : x + y

print(add(1, 2))
print(plus(1, 2))
