'''
callable(object)
判断对象是否可被调用
'''

class A:
    def __call__(self, *args, **kwargs):
        print("I'm a callable method")

a = A()

print(callable(a))
print(callable(A))


class B:
    pass

b = B()

print(callable(b))
print(callable(B))