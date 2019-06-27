'''
    vectorization
'''

from mxnet import nd
import time


def forLoopTime():
    start = time.time()

    a = nd.array(1000)
    b = nd.array(1000)

    c = nd.zeros(1000)
    for i in range(1000):
        c[i] = a[i] + b[i]
    end = time.time()
    print("Loop time: " + str(start - end) + "ms")


def vectorizationTime():
    start = time.time()
    a = nd.array(1000)
    b = nd.array(1000)
    c = nd.zeros(1000)
    c = a + b
    end = time.time()
    print("Vectorization time: " + str(start - end) + "ms")



vectorizationTime()






