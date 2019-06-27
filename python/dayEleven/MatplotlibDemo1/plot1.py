'''
    using matplotlib
'''
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-1, 1, 50)
print(x)
y = 2 * x + 1
y1 = x ** 2
plt.plot(x, y)
plt.plot(x, y1)
plt.show()