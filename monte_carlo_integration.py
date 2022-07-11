import random
import numpy as np
import matplotlib.pyplot as plt

a = 0
b = np.pi
N = 10000
times = 1000


def f(x):
    return np.sin(x)


y = []


def crude_monte_carlo(N):
    """
    Crude monte carlo method for calculating an integral
    :param N: a number for the iterations of the function
    :return: the integral
    """
    integral = 0.0
    for _ in range(N):
        x_i = random.uniform(a, b)
        integral += f(x_i)
    answer = (b - a) / float(N) * integral
    return answer


def experiment(times):
    """
    An experiment that runs the crude monte carlo for the input times
    creates a diagram of bars representing how many times the number was calculated from the crude method
    :param times: a number that represents the iterations the experiment is run
    :return: None
    """
    areas = []
    for _ in range(times):
        areas.append(crude_monte_carlo(N))
    plt.xlabel('x')
    plt.ylabel('density')
    plt.hist(areas, bins=31, ec="black")
    plt.show()


def monte_carlo(N):
    """
    A simple example of distributing points randomly and calculating how many points are inside the function then
    dividing the answer by the total number of points and multiplying by the distance of the function borders :param
    N: :return:
    """
    randy = np.random.uniform(0, 1, N)
    inside = 0
    for _ in range(N):
        color = "green"
        x_i, y_i = random.choice(randy), random.choice(randy)
        if y_i <= f(x_i):
            inside += 1
            color = "red"
        plt.plot(x_i, y_i, marker="o", markersize=1, markeredgecolor=color, markerfacecolor="green")
    print(f'Inside points: {inside} Outside points: {N - inside} Area:{(b - a) * inside / N}')
    x = np.linspace(0, 1, 1000)

    plt.plot(x, f(x))
    plt.show()


while True:

    try:
        op = int(input("Pick an option:\n1) Simple monte carlo\n2) Crude monte carlo\n3) Experiment\n"))

        if op == 1:
            monte_carlo(N)
            break
        elif op == 2:
            answer = crude_monte_carlo(N)
            print(f"The integral is: {answer}")
            break
        elif op == 3:
            experiment(times)
            break
        else:
            raise IndexError
    except IndexError:
        print("Incorrect number entered try again.")
    except ValueError:
        print("Not a number, try again.")
