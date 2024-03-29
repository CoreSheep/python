"""
    using inverted dropout to regularize linear regression model
"""
import MachineLearning.Utility.utils as tool
from mxnet import nd, autograd
from mxnet.gluon import loss as gloss


# define dropout function
def dropout(X, drop_prob):
    assert 0 <= drop_prob <= 1
    keep_prob = 1 - drop_prob
    if keep_prob == 0:
        return X.zeros_like()
    mask = nd.random.uniform(0, 1, X.shape) < keep_prob
    return mask * X


# define model parameters
num_inputs, num_outputs, num_hiddens1, num_hiddens2 = 784, 10, 256, 256

W1 = nd.normal(scale=0.01, shape=(num_inputs, num_hiddens1))
b1 = nd.zeros(shape=[num_hiddens1])

W2 = nd.normal(scale=0.01, shape=(num_hiddens1, num_hiddens2))
b2 = nd.zeros(shape=(num_hiddens2))

W3 = nd.normal(scale=0.01, shape=(num_hiddens2, num_outputs))
b3 = nd.zeros(num_outputs)

params = [W1, b1, W2, b2, W3, b3]
for param in params:
    param.attach_grad()


# define dropout probability
drop_prob1, drop_prob2 = 0.2, 0.5


# define model
def net(X):
    X = X.reshape(-1, num_inputs)
    H1 = (nd.dot(X, W1) + b1).relu()
    if autograd.is_training():
        H1 = dropout(H1, drop_prob1)
    H2 = (nd.dot(H1, W2) + b2).relu()
    if autograd.is_training():
        H2 = dropout(H2, drop_prob2)
    return nd.dot(H2, W3) + b3


# training model
num_epochs, lr, batch_size = 5, 0.5, 256
loss = gloss.SoftmaxCrossEntropyLoss()

train_iter, test_iter = tool.load_data_fashion_mnist(batch_size)
tool.train_ch3(net, train_iter, test_iter, loss, num_epochs, batch_size,
               params, lr)
