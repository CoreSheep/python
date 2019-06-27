# else 可用于 try .. else or while/for .. else

# try .. else
try:
    n1, n2 = input("input two nums: ")
    res = n1 / n2

except:
    print("Error ocurrs!")
else:
    print("res is " + res)
finally:
    print("Calculate Done\n")

# while .. else
i = eval(input("input a num: "))
while 0 <= i <=  5:
    print(i)
    i -= 1
else:
    print("out of range 0 ~ 5")

# for .. else
name = "SheepCore"
for c in name:
    if c == 'c':
        break
    print(c, end='')
else:
    print("For loop done.")