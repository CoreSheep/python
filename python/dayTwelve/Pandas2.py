'''
    using pandas
'''

import numpy as np
import pandas as pd


def createSeries():
    b = pd.Series(np.random.randn(5), ['a', 'b', 'c', 'd', 'e'])
    print(b)
    print(b.index)


def indexSeries():
    b = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
    print(b[1])
    print(b[0:3])
    print(b[[1, 3, 4]])
    print(b[b > b.median()])
    a = b[1:] + b[:-1]
    print(a)


def featureSeries():
    b = pd.Series([6, 7, 8, 9], index={'a': 6, 'b': 7, 'c': 8, 'd': 9})
    print(b)
    b.name = "new series"
    print(b.name)
    b.rename("rename")
    print(b.name)


def createDataFrame():
    # data with column-labels and indexes
    d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
         'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
    df = pd.DataFrame(d)
    print(df)

    # select some rows to display
    df1 = pd.DataFrame(d, index=['a', 'd'])
    print(df1)

    # add new column-labels
    df2 = pd.DataFrame(d, index=['a', 'b'], columns=['two', 'three', 'four'])
    print(df2)

    print("index: {}, columns: {}".format(df2.index, df2.columns))


createDataFrame()



