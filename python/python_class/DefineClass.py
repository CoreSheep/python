'''
    define a class
'''

class mylist(list):
    pass

ls = mylist()
for i in range(3):
    ls.append(i)
print("ls: ", ls)
ls.reverse()
print("reverse ls: ", ls)
