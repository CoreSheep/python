'''
    a simple demo implementing logistic regression using NDArray and autograd
'''

from IPython import display
from matplotlib import pyplot as plt
from mxnet import autograd, nd
import random


def data_set():
    num_inputs = 2              # feature nums
    num_examples = 1000         # sample nums
    true_w = [2, -3.4]          # weight nums
    true_b = 4.2                # bias
    features = nd.random.normal(scale=1, shape=(num_examples, num_inputs))
    labels = true_w[0] * features[:, 0] + true_w[1] * features[:, 1] + true_b
    # print(labels)
    labels += nd.random.normal(scale=0.01, shape=labels.shape)
    print(labels[0:3])
    print(features[0:3])
    return features, labels


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
    features, labels = data_set()
    draw(features, labels)
