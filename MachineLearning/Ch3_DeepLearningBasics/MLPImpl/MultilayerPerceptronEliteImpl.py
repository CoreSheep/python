'''
    a simpler multilayer perceptron model implementation
'''
import MachineLearning.Utility.utils as tool
from mxnet import gluon, init
from mxnet.gluon import loss as gloss, nn

# define model
net = nn.Sequential()

# add a full-connected hidden layer into the multilayer perception model
net.add(nn.Dense(256, activation='relu'))
net.add(nn.Dense(10))
net.initialize(init.Normal(sigma=0.01))

# training our multilayer model
batch_size = 256
train_iter, test_iter = tool.load_data_fashion_mnist(batch_size)

loss = gluon.loss.SoftmaxCrossEntropyLoss()
trainer = gluon.Trainer(net.collect_params(), 'sgd', {'learning_rate': 0.001})

num_epochs = 3

# training model begin
tool.train_ch3(net, train_iter, test_iter, loss, num_epochs, batch_size,
               None, None, trainer)

