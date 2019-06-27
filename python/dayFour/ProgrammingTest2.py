'''
100 以内的素数和
'''

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

sum = 0
for i in range(2, 100):
    if is_prime(i):
        sum += i
        print(i)
print(sum)

