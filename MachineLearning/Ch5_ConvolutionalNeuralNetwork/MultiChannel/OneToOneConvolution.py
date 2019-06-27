"""
    one to one convolutional neural network
"""

import MachineLearning.Utility.utils as tool
from mxnet import nd
from MachineLearning.Ch5_ConvolutionalNeuralNetwork.MultiChannel.MultiChannel\
    import corr2d_multi_in_out


def corr2d_multi_in_out_1x1(X, K):
    c_i, h, w = X.shape
    c_o = K.shape[0]
    X = X.reshape((c_i, h * w))
    K = K.reshape((c_o, c_i))
    Y = nd.dot(K, X)        # 全连接层的矩阵乘法
    return Y.reshape((c_o, h, w))


X = nd.random.uniform(shape=(3, 3, 3))
K = nd.random.uniform(shape=(2, 3, 1, 1))
Y1 = corr2d_multi_in_out_1x1(X, K)
Y2 = corr2d_multi_in_out(X, K)
print((Y1 - Y2).norm().asscalar() < 1e-6)