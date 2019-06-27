"""
    softmax implement
"""

import MachineLearning.Utility.utils as tool
from mxnet import autograd, nd

# load dataset(training dataset and test dataset)
batch_size = 256

# train_iter and test_iter represent two DataLoader objects
train_iter, test_iter = tool.load_data_fashion_mnist(batch_size)

print(train_iter, type(train_iter))

# d = 28 * 28 = 784, q = 10
num_inputs = 784
num_outputs = 10
# w.shape: (784, 10)  b.shape: (1, 10)
W = nd.random.normal(scale=0.01, shape=(num_inputs, num_outputs))
b = nd.zeros(num_outputs)
W.attach_grad()
b.attach_grad()


def softmax(X):
    X_exp = X.exp()
    partition = X_exp.sum(axis=1, keepdims=True)
    return X_exp / partition    # 这里应用了广播机制


def net(X):
    return softmax(nd.dot(X.reshape((-1, num_inputs)), W) + b)


def cross_entropy(y_hat, y):
    return -nd.pick(y_hat, y).log()


def accuracy(y_hat, y):
    return (y_hat.argmax(axis=1) == y.astype('float32')).mean().asscalar()


def evaluate_accuracy(data_iter, net):
    acc_sum, n = 0.0, 0
    for X, y in data_iter:
         y = y.astype('float32')
         acc_sum += (net(X).argmax(axis=1) == y).sum().asscalar()
         n += y.size
    return acc_sum / n


num_epochs, lr = 5, 0.1
tool.train_ch3(net, train_iter, test_iter, cross_entropy, num_epochs,
               batch_size, [W, b], lr)

for X, y in test_iter: 
    break

print(X.asnumpy().shape)

true_labels = tool.get_fashion_mnist_labels(y.asnumpy())
pred_labels = tool.get_fashion_mnist_labels(net(X).argmax(axis=1).asnumpy())
titles = [true + '\n' + pred for true, pred in zip(true_labels, pred_labels)]
tool.show_fashion_mnist(X[0:9], titles[0:9])