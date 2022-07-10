import random
import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 1
N = 2500
xrand = np.zeros(N)
for i in range(len(xrand)):
    xrand[i] = random.uniform(a, b)

def func(x):
    return x**2

areas = []

for _ in range(N):
    integral = 0.0
    for _ in range(N):
        integral += func(random.uniform(a, b))
    areas.append((b-a)/float(N)*integral)
plt.title("Distribution of Areas calculated")
plt.hist(areas, bins=31, ec='black')
plt.xlabel("Areas")
plt.show()

