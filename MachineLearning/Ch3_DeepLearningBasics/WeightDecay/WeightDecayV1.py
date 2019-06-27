'''
    using weight decay method to get rid of overfitting in
    high-dimensional linear regression
'''
import MachineLearning.Utility.utils as tool
from mxnet import autograd, gluon, init, nd
from mxnet.gluon import data as gdata, loss as gloss, nn


# 1. prepare training dataset
n_train, n_test, num_inputs = 20, 100, 200
true_w, true_b = nd.ones((num_inputs, 1)) * 0.01, 0.05
features = nd.random.normal(shape=(n_train + n_test, num_inputs))
labels = nd.dot(features, true_w) + true_b
labels += nd.random.normal(scale=0.01, shape=labels.shape)  # 噪声项
train_features, test_features = features[:n_train, :], features[n_train:, :]
train_labels, test_labels = labels[:n_train], labels[n_train:]


# 2. initialize model parameters
def init_params():
    w = nd.random.normal(scale=1, shape=(num_inputs, 1))
    b = nd.zeros(shape=(1,))
    w.attach_grad()
    b.attach_grad()
    return [w, b]


# 3. define L2 norm penalty
def l2_penalty(w):
    return (w ** 2).sum() / 2


# 4. training model and test
batch_size, num_epochs, lr = 1, 100, 0.003
net, loss = tool.linreg, tool.squared_loss
train_iter = gdata.DataLoader(gdata.ArrayDataset(
    train_features, train_labels), batch_size, shuffle=True)


def fit_and_plot(lambd):
    w, b = init_params() 
    train_ls, test_ls = [], [] 
    for _ in range(num_epochs):
        for X, y in train_iter: 
            with autograd.record():
                # 添加了L2范数惩罚项
                l = loss(net(X, w, b), y) + lambd * l2_penalty(w)
            l.backward()
            tool.sgd([w, b], lr, batch_size)
        train_ls.append(loss(net(train_features, w, b),
        train_labels).mean().asscalar())
        test_ls.append(loss(net(test_features, w, b),
        test_labels).mean().asscalar())
    tool.semilogy(range(1, num_epochs + 1), train_ls, 'epochs', 'loss',
                 range(1, num_epochs + 1), test_ls, ['train', 'test'])
    print('L2 norm of w:', w.norm().asscalar())


# 5. observe training results
fit_and_plot(lambd=0)

# 6. using weight decay
fit_and_plot(lambd=5)
