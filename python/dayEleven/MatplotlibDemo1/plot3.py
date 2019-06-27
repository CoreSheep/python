'''
    using pyplot
'''

import matplotlib.pyplot as plt
import numpy as np


def onlyAxisY():
    plt.plot([1, 2, 3, 4])
    plt.ylabel("some numbers")
    plt.show()



def drawWithAxis_X_Y():
    plt.plot([1, 2, 3, 4], [6, 7, 8, 9])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


drawWithAxis_X_Y()