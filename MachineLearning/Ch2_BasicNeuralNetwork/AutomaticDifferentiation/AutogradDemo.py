'''
    Automatic Differentiation
'''

from mxnet import autograd, nd

x = nd.arange(4).reshape((4, 1))
print(x)

# apply for the memory for storing gratitude
x.attach_grad()

global y
with autograd.record():
    y = 2 * nd.dot(x.T, x)
print(y)
print(y.backward())

assert (x.grad - 4 * x).norm().asscalar() == 0
