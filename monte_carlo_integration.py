import random
import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 1
N = 10000
times = 1000


def f(x):
    return x**2


y = []


def crude_monte_carlo(start, end, N):
    """
    Crude monte carlo method for calculating an integral
    :param start: start border of the function
    :param end: end border of the function
    :param N: number of iterations
    :return: the integral from start to end
    """
    integral = 0.0
    for _ in range(N):
        x_i = random.uniform(start, end)
        integral += f(x_i)
    answer = (end - start) / float(N) * integral
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
        areas.append(crude_monte_carlo(a,b,N))
    plt.xlabel('x')
    plt.ylabel('density')
    plt.hist(areas, bins=31, ec="black")
    plt.show()


def r_a_monte_carlo(start, end, N):
    """
    A rejection acception monte carlo function that distributes points randomly and calculates how many points are inside
     the function then dividing the answer by the total number of points and multiplying by the distance of the function
      borders
       :param start: start border of the function
       :param end: end border of the function
       :param N: number of iterations
       :return: None
    """
    randy = np.random.uniform(start, end, N)
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


def stratified_sampling_monte_carlo(intervals, N):
    """
    a fuction that calculates an integral based on the stratified sampling method seperating the funcion that is
    integrated into intervals and calculates its integral by the crude method
     :param intervals: the number intervals the function is sliced
     :param N: the number of iterations the crude method works at
     :return: the total integral from a to b
    """
    distance = b-a
    interval = distance/intervals
    start = a
    total = 0
    while start < b:
        total += crude_monte_carlo(start, start+interval, N)
        start = start + interval
    return total


while True:
    try:
        op = int(input("Pick an option:\n1) Simple monte carlo\n2) Crude monte carlo\n3) stratified_sampling\n4) "
                       "experiment\n"))

        if op == 1:
            r_a_monte_carlo(a, b, N)
            break
        elif op == 2:
            answer = crude_monte_carlo(a, b, N)
            print(f"The integral is: {answer}")
            break
        elif op == 3:
            print("The integral is:", stratified_sampling_monte_carlo(3,N))
            break
        elif op == 4:
            experiment(times)
            break
        else:
            raise IndexError
    except IndexError:
        print("Incorrect number entered try again.")
    except ValueError:
        print("Not a number, try again.")
