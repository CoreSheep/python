'''
    a simple linear regression implement with package gluon
'''
import mxnet as mx
from mxnet import autograd, nd
from mxnet.gluon import data as gdata
from mxnet.gluon import nn
from mxnet import init
from mxnet.gluon import loss as gloss

# 1.create dataset
num_inputs = 2
num_examples = 1000
true_w = [2, -3.4]
true_b = 4.2
features = nd.random.normal(scale=1, shape=(num_examples, num_inputs))
labels = true_w[0] * features[:, 0] + true_w[1] * features[:, 1] + true_b
labels += nd.random.normal(scale=0.01, shape=labels.shape)

# 2.read dataset in a mini-batch way
batch_size = 10
# 将训练数据的特征和标签组合
dataset = gdata.ArrayDataset(features, labels)
# 随机读取小批量
data_iter = gdata.DataLoader(dataset, batch_size, shuffle=True)

# define our model
net = nn.Sequential()       # sequential 实例可以看成一个串联各个层的 container
net.add(nn.Dense(1))        # 添加一个全连接层 -- 线性回归输出层

# initialize model parameters
net.initialize(init.Normal(sigma=0.01))     # 参数初始化(weights and bias)

# define loss function
loss = gloss.L2Loss()       # 平方损失又称L2范数损失


# define optimization algorithm
trainer = mx.gluon.Trainer(net.collect_params(), 'sgd', {'learning_rate': 0.01})


# train the model with epochs of three
num_epochs = 3
for epoch in range(1, num_epochs + 1):
    for X, y in data_iter:
        with autograd.record():
            l = loss(net(X), y)
        l.backward()
        trainer.step(batch_size)
    l = loss(net(features), labels)
    print('epoch %d, loss: %f' % (epoch, l.mean().asnumpy()))


# check out the result of our training model
dense = net[0]
print(true_w, dense.weight.data())





