"""
    customize gluon layer
"""
from mxnet import gluon, nd, init
from mxnet.gluon import nn


class SheepCoreLayer(nn.Block):
    """ define customized layer without model parameters"""
    def __init__(self, **kwargs):
        # super(subclass, self).__init__(**kwargs)
        super(SheepCoreLayer, self).__init__(**kwargs)

    def forward(self, x):
        """ call automatically when net(X) execute """
        return x - x.mean()


mylayer = SheepCoreLayer()
X = nd.arange(5)
y_hat = mylayer(X)
print(y_hat)

# nest our customized layer into Sequential
net = nn.Sequential()
net.add(nn.Dense(256, activation='relu'),
        SheepCoreLayer(),
        nn.Dense(10))
net.initialize(init=init.Xavier())
print(net(X))


class MyDense(nn.Block):
    """ define customized layer with model parameters"""
    # units为该层的输出个数，in_units为该层的输入个数
    def __init__(self, units, in_units, **kwargs):
        super(MyDense, self).__init__(**kwargs)
        self.weight = self.params.get('weight', shape=(in_units, units))
        self.bias = self.params.get('bias', shape=(units,))

    def forward(self, x):
        linear = nd.dot(x, self.weight.data()) + self.bias.data()
        return nd.relu(linear)


dense = MyDense(units=3, in_units=5)
print(dense.params)





