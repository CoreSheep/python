"""
    using block initializer
"""

from mxnet import nd
from mxnet.gluon import nn


class MLP(nn.Block):
    """
    input layer
    hidden layer
    output layer
    """
    # define layers, here we defined two full-connected layers
    def __init__(self, **kwargs):
        super(MLP, self).__init__(**kwargs)
        self.hidden = nn.Dense(256, activation='relu')
        self.output = nn.Dense(10)

    def forward(self, X):
        return self.output(self.hidden(X))


X = nd.random.uniform(shape=(3, 4))
net = MLP()
net.initialize()
print(net.summary(X))
