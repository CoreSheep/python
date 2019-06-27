'''
    practice on Ndarray of Mxnet
'''

import mxnet as mx

# create and one-dimensional array
a = mx.nd.array(1000)
b = mx.nd.array(1000)

c = a + b

print(c)