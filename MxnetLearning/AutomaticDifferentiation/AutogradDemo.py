'''
    Automatic differentiation with autograd
'''

import mxnet as mx
from mxnet import nd, autograd
mx.random.seed(1)


def autogradV1():
    # z = 2 * (x ** 2)
    x = nd.array([[1, 2], [3, 4]])
    y = x * 2
    x.attach_grad()
    y.attach_grad()
    with autograd.record():
        y = x * 2
        z = y * x
    z.backward()
    print(x.grad)


def autogradV2():
    a = nd.random_normal(shape=3)
    a.attach_grad()

    with autograd.record():
        b = a * 2
        while (nd.norm(b) < 1000).asscalar():
            b = b * 2

        if (mx.nd.sum(b) > 0).asscalar():
            c = b
        else:
            c = 100 * b

    head_gradient = nd.array([0.01, 1.0, .1])
    c.backward(head_gradient)
    print(a.grad)


a = nd.norm()