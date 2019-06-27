'''
    using numpy
'''

# part one: basic numpy
import numpy as np


def arrayBasic():
    a = np.arange(15).reshape(3, 5)
    print(a)
    print("shape: {}".format(a.shape))          # rows and columns
    print("dimension: %s" % a.ndim)             # dimension: two-dimension array
    print("data type: %s" % a.dtype)            # data type
    print("Itemsize: %s" % a.itemsize)          # the bytes of elements
    print("size: %s" % a.size)                  # the size of total elements


# part two: Array Creation
def arrayCreation():
    # 1.通过列表创建
    a1 = np.array([1, 2, 3], dtype=np.int)
    print("a1.dtype: {}".format(a1.dtype))

    a2 = np.array((1, 2, 3), dtype=np.int32)
    print(a2)

    # wrong creation
    # a2 = np.array(1, 2, 3)
    # print(a2)

    # 2.通过二维列表创建array
    a3 = np.array([[1, 2, 3], [4, 5, 6]])
    print(a3)

    a4 = np.array([(1, 2, 3), (4, 5, 6)])
    print(a4)

    # 3.通过arange()创建有序的array
    a5 = np.arange(20).reshape(4, 5)
    print(a5)

    # create with specific data type
    a6 = np.array([(10, 11, 12, 13), (14, 15, 16, 17)], dtype=complex)
    print(a6)

    # 4.create from functions
    def liner(x, y):
        return 10 * x + y
    a7 = np.fromfunction(liner, (5, 4), dtype=int)
    print(a7)

    # 5.生成等距线段值
    a8 = np.linspace(0, 10, 20)
    print(a8)

def arrayInit():
    a0 = np.zeros(shape=(3, 4), dtype=complex)
    print(a0)
    print(a0.data)
    print(a0.shape)

    a1 = np.zeros(shape=(3, 4), dtype=np.int16)
    print(a1)
    print(a1.dtype)
    print(a1.ndim)

    a2 = np.ones(shape=[3, 4], dtype=np.float64)
    print(a2)

    a3 = np.empty((3, 4), np.float64)
    print(a3)

    # create arrays with slices
    a4 = np.arange(0, 20, 3)
    print(a4)
    a5 = np.arange(0, 3, 0.5)
    print(a5)


def arrayOperations():
    a0 = np.array([10, 20, 30, 40])
    b0 = np.arange(4)
    c0 = a0 - b0
    print(c0)
    print(b0 ** 2)
    print(a0 > 30)

    # simple product and matrix product
    a1 = np.array([(1, 1), (0, 1)])
    b1 = np.array([[2, 0], [3, 4]])
    print(a1 * b1)  # 数乘
    print(a1 @ b1)
    print(a1.dot(b1))  # 矩阵乘法

    # +=, *=, -=, /=
    a2 = np.array([(1, 1), (0, 1)])
    b2 = np.array([[2, 0], [3, 4]])
    a2 += 3
    b2 -= a2
    print(a2)
    print(b2)

    # min, max, sum
    a3 = np.arange(15).reshape(3, 5)
    print(a3)
    print(a3.sum())
    print(a3.sum(axis=0))  # 每一行中求和
    print(a3.max(axis=1))  # 每一列中的最大值
    print(a3.min(axis=0))  # 每一行中的最小值
    print(a3[:, 2:4])           # rows from first to last, columns from 2 to 3


def arrayTraverse():
    a0 = np.arange(0, 30, 2).reshape(3, 5)
    for row in a0:
        print(row)

    for e in a0.flat:
        print(e)


def arrayReshape():
    a0 = np.floor(10 * np.random.random((3, 4)))
    print(a0)
    print(a0.shape)
    print(a0.ravel())
    print(a0.T)

    a1 = a0.reshape((4, 3))
    a2 = a0.reshape(2, -1)
    print("a1: ", a1)
    print("a0: ", a0)
    print("a2: ", a2)


def arrayConcatenate():
    a = np.array([(1, 2), (3, 4)])
    b = np.array([(2, 1), (4, 3)])
    print(np.vstack((a, b)))
    print(np.hstack((a, b)))
    print(np.column_stack((a, b)))


def arraySplit():
    a = np.floor(10 * np.random.random((2, 12)))
    print(a)

    print(np.hsplit(a, 6))
    print(np.vsplit(a, 2))


def arrayCopy():
    a = np.arange(12)
    a.shape = 3, 4
    print(a)

    # view or shallow copy
    b = a
    print(b is a)
    print("id of a: %s" % id(a))
    print("id of b: %s" % id(b))

    b[0, 3] = 100
    print("a:\n{}".format(a))
    print("b:\n{}".format(b))

    c = a.view()
    print(c is a)
    print("id of c: %s" % id(c))

    # deep copy
    origin = np.arange(10, 20).reshape(2, 5)
    print("origin address: %s" % id(origin))
    copy = origin.copy()
    print("copy address: %s" % id(copy))
    print(copy)
    print("copy is origin {}".format(copy is origin))
    print(("copy.base is origin {}".format(copy.base is origin)))

    copy[0, 4] = 100
    print(origin)
    print(copy)


def arrayIndice():
    a = np.arange(12)
    print(a)
    i = np.array([0, 3, 4, 5])
    print(a[i])

    a.shape = 2, 6
    print(a)
    i = np.array([[0, 0], [1, 1]])
    j = np.array([[3, 4], [3, 4]])
    print(a[i, j])


def operations2():
    '''
    argmin
    argmax
    cumsum
    diff
    mean and average
    nonzero
    sort
    transpose: 矩阵转置
    clip:

    :return:
    '''
    a = np.arange(14, 2, -1).reshape((3, 4))
    print(a)

    print("最大元素索引: ", a.argmax())
    print("最小元素索引: ", a.argmin())
    print("累加值: ", a.cumsum())
    print("累差值: \n", np.diff(a))  # 后一个减去前一个
    print("平均值: ", np.mean(a))
    print("平均值: ", np.average(a))
    print("排序: \n", np.sort(a))
    print("转置:\n", np.transpose(a))
    print("返回非零元素位置:\n ", np.nonzero(a))
    print("clip:(保留5～9）\n", a.clip(5, 9))


def indexDemo2():
    a = np.arange(3, 15).reshape(3, 4)
    # 1.print all elements
    print(a)

    # 2.print single element
    print(a[0, 0])
    print(a[0][1])

    # 3.print each row
    for row in a:
        print(row)

    # 4.print each column
    for column in a.T:  # notice the T is uppercase!
        print(column)

    # 5.print each item
    for item in a.flat: # a.flat is one dimensional array with an iterator
        print(item)


def mergeDemo1():
    '''
    1.vstack
    2.hstack
    3.newaxis
    4.concatenate

    :return:
    '''
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    print(a, a.shape)
    print(b, b.shape)

    c = np.vstack((a, b))       # vertical stack
    print(c, c.shape)

    a1 = a[:, np.newaxis]       # horizontal stack
    b1 = b[:, np.newaxis]
    d = np.hstack((a1, b1))
    print(d)

    print(np.concatenate((a[:, np.newaxis], b[:, np.newaxis]), axis=1))


def splitDemo1():
    a = np.arange(12).reshape(3, 4)
    print(a)

    # 1.split vertically(only split equally)
    print(np.split(a, 2, axis=1))   # we got two [3][2] arrays
    # print(np.vsplit(a, 2))

    # 2.split horizontally(only split equally)
    print(np.split(a, 3))   # we got three [1][4] arrays
    # print(np.hsplit(a, 3))

    # 3.split at will
    print(np.array_split(a, 3, axis=1))


splitDemo1()













