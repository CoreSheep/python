'''
    Travelling Salesman Problem with Simulated annealing algorithm
'''

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

# 计算两点距离的函数
def CalDistance(x,y):
    return math.sqrt(x**2+y**2)

# 计算当前路径中的总长度
def CalLength(citys, paths, start, end):
    '''

    :param citys:
    :param paths:
    :param start:
    :param end:
    :return:
    '''
    length=0
    n=1
    for i in range(len(paths)):
        if i==0:
            # 起点到第一个途径城市的距离
            length+=CalDistance(start[0]-citys['x'][paths[i]],start[1]-citys['y'][paths[i]])
            n+=1
        elif n<len(paths):
            # 途径中间城市i和城市i+1的距离
            length+=CalDistance(citys['x'][paths[i]]-citys['x'][paths[i+1]],citys['y'][paths[i]]-citys['y'][paths[i+1]])
            n+=1
        else:
            # 最后一个途径城市到终点的距离
            length+=CalDistance(citys['x'][paths[i]]-end[0],citys['y'][paths[i]]-end[1])
    return length


# 读取文件，并打印文件数据示例
citys = pd.read_table('data.txt', sep='\t', header=None)
citys.columns = ['x']
citys['y'] = None

for i in range(len(citys)):
    coordinate = citys['x'][i].split()
    citys['x'][i] = float(coordinate[0])
    citys['y'][i] = float(coordinate[1])

print(citys.head(5))  # 打印前5个