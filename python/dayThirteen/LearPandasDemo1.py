'''
    using pandas
'''

import numpy as np
import pandas as pd


def getstartedPandas():
    s = pd.Series([1, 3, 5, np.nan, 8, 10], dtype=np.float32)
    print(s)

    dates = pd.date_range('20190530', periods=7)
    print(dates)

    # Creating a DataFrame by passing a NumPy array,
    # with a datetime index and labeled columns:
    df = pd.DataFrame(np.random.randn(7, 4), index=dates, columns=list('ABCD'))
    print(df)
    print(df.dtypes)
    print("DataFrame Head: \n", df.head(2))

    print("DataFrame Tail: \n", df.head(3))

    print("array:\n", df.to_numpy(), df.to_numpy().ndim)

    # describe() shows a quick statistic summary of your data:
    print(df.describe())




getstartedPandas()


