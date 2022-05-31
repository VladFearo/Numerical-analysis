import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x**3-4*x**2-1


y = np.linspace(-2,5)  # טווח להדפסה
plt.plot(y, f(y))
plt.show()
