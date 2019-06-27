"""
    training data with softmax model
"""
import MachineLearning.Utility.utils as tool
from mxnet.gluon import data as gdata
from mxnet import nd
import sys
import time

# Mixed National Institute of Standards and Technology database
mnist_train = gdata.vision.FashionMNIST(train=True)
mnist_test = gdata.vision.FashionMNIST(train=False)

feature, labels = mnist_train[0]

X, y = mnist_train[0: 9]
tool.show_fashion_mnist(X, tool.get_fashion_mnist_labels(y))


# read with mini-batch size
batch_size = 256
transformer = gdata.vision.transforms.ToTensor()
if sys.platform.startswith('win'):
    num_workers = 0  # 0表示不用额外的进程来加速读取数据
else:
    num_workers = 4
train_iter = gdata.DataLoader(mnist_train.transform_first(transformer),
                              batch_size, shuffle=True, num_workers=num_workers)
test_iter = gdata.DataLoader(mnist_test.transform_first(transformer),
                             batch_size, shuffle=False, num_workers=num_workers)

# check out the time of retrieving data from data_iter
start = time.time()
for X, y in train_iter:
    continue
print('%.2f sec' % (time.time() - start))


