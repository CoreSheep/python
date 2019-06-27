"""
    model parameters accessing
"""

from mxnet import init, nd
from mxnet.gluon import nn

net = nn.Sequential()
net.add(nn.Dense(256, activation='relu'))
net.add(nn.Dense(10))
net.initialize()  # 使用默认初始化方式
X = nd.random.uniform(shape=(2, 20))
y_hat = net(X)  # 前向计算


def showParams():
    """ access model parameters """
    # something about params in net
    # print the weight parameters in dense 0(hidden layer)
    print(net[0].params, type(net[0].params))
    print(net[0].params['dense0_weight'], )

    # print weight data and grad
    print(net[0].params['dense0_weight'].data(),
          net[0].params['dense0_weight'].grad)

    # get dense1 layer
    print(net[1].params['dense1_weight'], type(net[1].params['dense1_weight']))

    # get all params
    print(net.collect_params())


""" initialize model parameters """
# 非首次对模型初始化需要指定 force_reinit 为真
# 1.正太函数初始化
net.initialize(init=init.Normal(sigma=0.01), force_reinit=True)
print(net[0].weight.data()[0])
# 2.常数初始化
net.initialize(init=init.Constant(-1), force_reinit=True)
print(net[0].weight.data()[0])

# 3.对某一层参数进行初始化
net[0].weight.initialize(init=init.Xavier(), force_reinit=True)
print(net[0].weight.data()[0])


class MyInit(init.Initializer):
    def _init_weight(self, name, data):
        print('Init', name, data.shape)
        data[:] = nd.random.uniform(low=-10, high=10, shape=data.shape)
        data *= data.abs() >= 5


# 4.using customized initializer to init model parameters
net.initialize(MyInit(), force_reinit=True)
print(net[0].weight.data()[0])


""" share model parameters """
net = nn.Sequential()
shared = nn.Dense(8, activation='relu')
net.add(nn.Dense(8, activation='relu'),
        shared,         # share layer
        # share the shared params in layer shared
        nn.Dense(8, activation='relu', params=shared.params),
        nn.Dense(10))
net.initialize()


