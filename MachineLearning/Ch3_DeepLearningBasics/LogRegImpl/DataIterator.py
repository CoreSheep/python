'''
    data iterator
'''

import mxnet as mx

a = mx.nd.arange(12).reshape(6, 2)
b = mx.nd.ones((6, 1))

print(a)
print(b)

indice = [1, 3, 4]

print(a.take(mx.nd.array(indice)))
print(b.take(mx.nd.array(indice)))
