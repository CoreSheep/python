'''
    a simple demo implementing logistic regression using NDArray and autograd
'''

from IPython import display
from matplotlib import pyplot as plt
from mxnet import autograd, nd
import random

# global variables
num_inputs = 2  # feature nums
num_examples = 1000  # sample nums
batch_size = 10


def data_set():
    true_w = [2, -3.4]          # weight nums
    true_b = 4.2                # bias
    features = nd.random.normal(scale=1, shape=(num_examples, num_inputs))
    labels = true_w[0] * features[:, 0] + true_w[1] * features[:, 1] + true_b
    # print(labels)
    labels += nd.random.normal(scale=0.01, shape=labels.shape)
    return features, labels


def data_iter(batch_size, features, labels):
    num_examples = len(features)
    indices = list(range(num_examples))
    random.shuffle(indices)     # randomly read sample
    for i in range(0, num_examples, batch_size):      # batch nums
        j = nd.array(indices[i: min(i + batch_size, num_examples)])
        yield features.take(j), labels.take(j)  # return and generator


# vectorization of linear regression
def linreg(X, w, b):
    return nd.dot(X, w) + b


def squared_loss(y_hat, y):
    return (y_hat - y.reshape(y_hat.shape)) ** 2 / 2


def sgd(params, lr, batch_size):
    for param in params:
        param[:] = param - lr * param.grad / batch_size


def use_svg_display():
    # using Scalable Vector Graphics format
    display.set_matplotlib_formats('svg')


def set_figsize(figsize=(3.5, 2.5)):
    use_svg_display()
    # set figure size
    plt.rcParams['figure.figsize'] = figsize


def draw(features, labels):
    set_figsize()
    plt.scatter(features[:, 1].asnumpy(), labels.asnumpy(), 1)  # 加分号只显示图
    plt.show()


if __name__ == '__main__':
    w = nd.random.normal(loc=0, scale=0.01, shape=(num_inputs, 1))
    b = nd.zeros(shape=(1,))
    w.attach_grad()
    b.attach_grad()
    lr = 0.02
    num_epochs = 3
    net = linreg
    loss = squared_loss
    features, labels = data_set()

    # 在每一个迭代周期中，会使用训练数据集中所有样本一次(假设样本数能够被批量大小整除)。X
    # 和y分别是小批量样本的特征和标签
    for epoch in range(num_epochs):  # 训练模型一共需要num_epochs个迭代周期
        for X, y in data_iter(batch_size, features, labels):
            with autograd.record():
                los = loss(net(X, w, b), y)  # l是有关小批量X和y的损失
            los.backward()  # 小批量的损失对模型参数求梯度
            sgd([w, b], lr, batch_size)  # 使用小批量随机梯度下降迭代模型参数
        train_l = loss(net(features, w, b), labels)
        print('epoch %d, loss %f' % (epoch + 1, train_l.mean().asnumpy()))
