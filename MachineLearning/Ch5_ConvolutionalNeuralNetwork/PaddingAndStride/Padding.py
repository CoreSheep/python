"""
    padding
"""
from mxnet import nd
from mxnet.gluon import nn


# 定义一个函数来计算卷积层。它初始化卷积层权重，并对输入和输出做相应的升维和降维
def comp_conv2d(conv2d, X):
    conv2d.initialize()
    # (1, 1)代表批量大小和通道数(“多输入通道和多输出通道”一节将介绍)均为1
    X = X.reshape((1, 1) + X.shape)     # (1, 1, height, width)
    Y = conv2d(X)
    return Y.reshape(Y.shape[2:])       # 排除不关心的前两维:批量和通道


# 注意这里是两侧分别填充1行或列，所以在两侧一共填充2行或列
conv2d = nn.Conv2D(1, kernel_size=3, padding=1)
X = nd.random.uniform(shape=(8, 8))
Y = comp_conv2d(conv2d, X).shape
print(Y)


conv2d = nn.Conv2D(1, kernel_size=(3, 5), padding=(1, 2))
Y2 = comp_conv2d(conv2d, X).shape
print(Y2)

conv2d = nn.Conv2D(1, kernel_size=3, padding=1, strides=4)
Y3 = comp_conv2d(conv2d, X).shape
print(Y3)

conv2d = nn.Conv2D(1, kernel_size=(3, 5), padding=(0, 1), strides=(3, 4))
Y4 = comp_conv2d(conv2d, X).shape
print(Y4)
