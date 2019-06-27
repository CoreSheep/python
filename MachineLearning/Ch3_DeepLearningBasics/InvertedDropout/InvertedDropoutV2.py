"""
    using inverted dropout to regularize linear regression model with gluon
"""

import MachineLearning.Utility.utils as tool
from mxnet import nd, autograd, gluon, init
from mxnet.gluon import loss as gloss, nn

# global flag
Horizontal = 1
Vertical = 0

# define dropout probability
drop_prob1, drop_prob2 = 0.2, 0.5

# define model
# neural networks container
net = nn.Sequential()
# construct neural network layers
net.add(nn.Dense(256, activation='relu'),
        nn.Dropout(drop_prob1),
        nn.Dense(256, activation='sigmoid'),
        nn.Dropout(drop_prob2),
        nn.Dense(10))
# initialize model parameters
net.initialize()


def sgd(params, lr, batch_size):
    for param in params:
        param[:] = param - lr * param.grad / batch_size


def train_sheepcore(net, train_iter, test_iter, loss, num_epochs, batch_size,
                    params=None, lr=None, trainer=None):
    for epoch in range(num_epochs):
        train_l_sum, train_acc_sum, n = 0.0, 0.0, 0
        for X, y in train_iter:
            with autograd.record():
                y_hat = net(X)
                l = loss(y_hat, y).sum()
            l.backward()
            if trainer is None:
                tool.sgd(params, lr, batch_size)
            else:
                trainer.step(batch_size)
            y = y.astype('float32')
            train_l_sum += l.asscalar()
            train_acc_sum += (y_hat.argmax(axis=Horizontal) == y).sum().asscalar()
            n += y.size
        print('epoch %d, loss %.4f, train_acc %.3f'
              % (epoch, train_l_sum / n, train_acc_sum / n))


# training model
num_epochs, lr, batch_size = 5, 0.5, 256
loss = gloss.SoftmaxCrossEntropyLoss()
train_iter, test_iter = tool.load_data_fashion_mnist(batch_size)
trainer = gluon.Trainer(net.collect_params(), 'sgd', {'learning_rate': lr})
train_sheepcore(net, train_iter, test_iter, loss, num_epochs, batch_size,
               params=None, lr=None, trainer=trainer)