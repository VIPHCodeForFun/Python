# Vidmar P.
# pip install matplotlib
# pip install numpy

import matplotlib.pyplot as plt
import numpy as np


def f(x):
    temp = np.cos(2*np.pi*x)
    return temp


x = np.arange(0.0, 5.0, 0.1)

plt.subplot(211)
plt.plot(x, np.cos(2*np.pi*x), 'r--')

# ---------------------------------------------

plt.grid()
plt.ylabel('some Y numbers')
plt.xlabel('some X numbers')

# ---------------------------------------------

plt.subplot(212)
plt.plot(x, f(x), 'b')

# ---------------------------------------------

plt.grid()
plt.ylabel('some Y numbers')
plt.xlabel('some X numbers')

# ---------------------------------------------

plt.show()
