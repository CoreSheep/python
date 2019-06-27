'''
    implement softmax model in a simple way
'''

from MachineLearning.Utility import utils as tool
from mxnet import gluon, init
from mxnet.gluon import loss as gloss, nn

# load data
batch_size = 256
train_iter, test_iter = tool.load_data_fashion_mnist(batch_size)

# define and initialize model
net = nn.Sequential()
net.add(nn.Dense(10))
net.initialize(init.Normal(sigma=0.01))


# define loss function
loss = gloss.SoftmaxCrossEntropyLoss()

# using sgd to optimize
trainer = gluon.Trainer(net.collect_params(), 'sgd', {'learning_rate': 0.1})

# training our model automatically
num_epochs = 5
tool.train_ch3(net, train_iter, test_iter, loss, num_epochs, batch_size, None,
               None, trainer)


