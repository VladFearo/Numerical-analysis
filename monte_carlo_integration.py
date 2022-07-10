import random
import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 1
N = 10000


def f(x):
    return x ** 2


y = []



def monte_carlo(N):
    integral = 0.0
    for _ in range(N):
        x_i = random.uniform(a, b)
        integral += f(x_i)
    return (b - a) / float(N) * integral

areas = []
for _ in range(1000):
    areas.append(monte_carlo(N))
plt.figure(figsize=(8, 5))
x = np.linspace(0, 1, 1000)
# plt.plot(x, f(x))
randy = np.random.uniform(0, 1, N)

inside = 0
"""for _ in range(10000):
    color = "green"
    x_i, y_i = random.choice(randy), random.choice(randy)
    if y_i <= f(x_i):
        inside += 1
        color = "red"
    #plt.plot(x_i, y_i, marker="o", markersize=1, markeredgecolor=color, markerfacecolor="green")"""
#print(f'Inside points: {inside} Outside points: {N - inside} Area:{(b - a) * inside / N}')
plt.xlabel('x')
plt.ylabel('density')
plt.hist(areas, bins=30, ec="black")
plt.show()
