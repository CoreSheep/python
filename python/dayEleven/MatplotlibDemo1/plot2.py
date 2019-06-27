'''
    using matplotlib
'''
import numpy as np
import matplotlib.pyplot as plt


def simpleLine():
    x = np.linspace(0, 2, 100)
    plt.title("Simple Plot")
    plt.plot(x, x, label='linear')
    plt.plot(x, x ** 2, label='quadratic')
    plt.plot(x, x ** 3, label='cubic')

    plt.xlabel("x label")
    plt.ylabel("y label")
    plt.legend()
    plt.show()


def simpleSin():
    x = np.arange(0, 10, 0.2)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()


def subplots1():
    x = np.arange(0.1, 100)

    # axe1
    plt.subplot(221)
    plt.plot(x, x)

    # axe2
    plt.subplot(222)
    plt.plot(x, -x)

    # axe3
    plt.subplot(223)
    plt.plot(x, x ** 2)
    plt.grid(color='r', linestyle='--', linewidth=1, alpha=0.3)

    # axe4
    plt.subplot(224)
    plt.plot(x, np.log(x))
    plt.show()


def subplots2():
    x = np.arange(1, 100)
    # divided into subplots
    fig, axes = plt.subplots(2, 2)
    ax1 = axes[0, 0]
    ax2 = axes[0, 1]
    ax3 = axes[1, 0]
    ax4 = axes[1, 1]

    # plot1
    ax1.plot(x, x)
    # plot2
    ax2.plot(x, -x)
    # plot3
    ax3.plot(x, x ** 2)
    ax3.grid(color='r', linestyle='--', linewidth=1, alpha=0.3)
    # plot4
    ax4.plot(x, np.log(x))
    plt.show()




subplots2()