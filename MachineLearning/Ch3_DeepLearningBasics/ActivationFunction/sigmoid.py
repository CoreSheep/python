"""
    sigmoid -- activation function
"""

from MachineLearning.Utility import utils as tool
from mxnet import autograd, nd


def xyplot(x_vals, y_vals, name):
    tool.set_figsize(figsize=(5, 2.5))
    tool.plt.plot(x_vals.asnumpy(), y_vals.asnumpy())
    tool.plt.xlabel('x')
    tool.plt.ylabel(name + '(x)')
    tool.plt.show()


# global variables
x = nd.arange(16).reshape(4, 4)
print(x)
print(x.sum(axis=0))
print(x.argmax(axis=1).sum().asscalar())
l = x.sum().asscalar()
print(l)


def sigmoid():
    with autograd.record():
        y = x.sigmoid()
    xyplot(x, y, 'sigmoid')
    y.backward()
    xyplot(x, x.grad, 'grad of sigmo')