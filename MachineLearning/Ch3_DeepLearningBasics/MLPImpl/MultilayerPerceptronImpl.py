'''
    a simple implementation of multilayer perceptron model

'''

import MachineLearning.Utility.utils as tool
from mxnet import nd
from mxnet.gluon import loss as gloss

# 1.read dataset
batch_size = 256
train_iter, test_iter = tool.load_data_fashion_mnist(batch_size)

# 2.define model parameters
num_inputs, num_outputs, num_hiddens = 784, 10, 256
W1 = nd.random.normal(scale=0.01, shape=(num_inputs, num_hiddens))
b1 = nd.zeros(num_hiddens)
W2 = nd.random.normal(scale=0.01, shape=(num_hiddens, num_outputs))
b2 = nd.zeros(num_outputs)
params = [W1, b1, W2, b2]

for param in params:
    param.attach_grad()


# 3.define activation function
def relu(X):
    return nd.maximum(X, 0)


# 4.define model
def net(X):
    X = X.reshape((-1, num_inputs))
    H = relu(nd.dot(X, W1) + b1)
    return nd.dot(H, W2) + b2


# 5.define loss function
loss = gloss.SoftmaxCrossEntropyLoss()


# 6.training model
num_epochs, lr = 5, 0.5
tool.train_ch3(net, train_iter, test_iter, loss, num_epochs, batch_size,
               params, lr)


