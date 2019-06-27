'''
    using pandas
'''

import pandas as pd
import numpy as np

b = pd.Series(['a', 'b', 'c', 'd'])
print(b)

b = pd.Series([1, 2, 3, 4], index=[4, 5, 6, 7])
print(b)

b = pd.Series(25, index=[0, 1, 2, 3, 4, 5])
print(b)

b = pd.Series({'a': 9, 'b': 8, 'c': 7})
print(b)

b = pd.Series({'a': 9, 'b': 8, 'c': 7}, index=['c', 'a', 'b', 'd'])
print(b)

b = pd.Series(np.arange(5), index=np.arange(10, 5, -1))
print(b)
print(b[[10, 7, 6]])
print(b[b > b.median()])
print(b[:3])
print('c' in b)
print(10 in b)