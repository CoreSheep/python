"""
    save and load dataset
"""
from mxnet import nd
from mxnet.gluon import nn

# save data to file
x = nd.ones(3)
nd.save('x', x)

# load data from file
x2 = nd.load('x')
print(x2)

y = nd.zeros(4)
nd.save('xy', [x, y])
x2, y2 = nd.load('xy')
print(x2, y2)

# save dict data to file
mydict = {'x': x, 'y': y}
nd.save('mydict', mydict)
mydict2 = nd.load('mydict')
print(mydict2)


# read Gluon params
class MLP(nn.Block):
    def __init__(self, **kwargs):
        super(MLP, self).__init__(**kwargs)
        self.hidden = nn.Dense(256, activation='relu')
        self.output = nn.Dense(10)

    def forward(self, x):
        return self.output(self.hidden(x))


net = MLP()
net.initialize()
X = nd.random.uniform(shape=(2, 20))
Y = net(X)

# save model parameters
filename = 'mlp.params'
net.save_parameters(filename)

# load model parameters
net2 = MLP()
net2.load_parameters(filename)
Y2 = net2(X)
print(Y2 == Y)

