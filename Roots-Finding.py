import math

import sympy as sp

def deriv_poly(poly):
    """
    derives a polynomial list (e.g. [1,2,3] -> x^2+2x+3
    :param poly: a list of numbers representing a function
    :return: a list of numbers representing a function after derivation
    """
    deriv = []
    n = len(poly)
    for x in poly:
        n -= 1
        if n !=0:
            deriv.append(x * n)
    return deriv


def bisection_method(a, b, f,epsilon):
    """
    returns an intersection point between a function and the x axis between point a and b using the bisection method
    :param a: a number repressenting a point on the x axis
    :param b: a number repressenting a point on the x axis
    :param f: a python function repressenting a polynomail function
    :return: a number repressenting the intersection point between the fucntion and the x axis
    """
    global i
    m = (a+b)/2

    print(f'Iter {i}: {m}')
    i += 1
    if round(f(m), 5) != 0:
        if f(a) * f(m) < 0:
            return bisection_method(a, m, f,epsilon)
        elif f(m) * f(b) < 0:
            return bisection_method(m, b, f,epsilon)
        else:
            i = 1
    else:
        i = 1
        return round(m, 3)

i = 1


def create_poly_func(f):
    """
    creates a python function repressenting a polynomial function
    :param f: a list repressenting a polynomial function
    :return: a python function repressenting a polynomial function
    """

    def func(x):
        # if derive_check == 1:
        #     n = len(f)
        # else:
        n = len(f) - 1
        solution = 0
        for poly in f:
            solution += poly * (x ** n)
            n -= 1
        return solution

    return func

def newton_raphson(a, b, f, epsilon):
    #test = (a+b)/2
    i = 1
   # if f(a) > 0 > f(b) or f(a) < 0 < f(b):
    while True:
        if(f_d(a)) == 0: #divide by zero
            break
        x1 = a - f(a) / f_d(a)
        print(f'Iter{i}. {x1}')
        i += 1
        a = x1
        if abs(f(x1)) < epsilon:
            return round(x1, 3)

    # else:
    #     return

def secant_method(a, b, f, epsilon):
    """
    An iterative method function for finding the roots
    of a continuous function of one variable.
    :param a: Start point of the test range
    :param b: End point of the test range
    :param f: Polynomial function
    :param epsilon: Epsilon for solution accuracy
    :return: The root we were looking for in the given test range
    """
    i = 1
    N = 30
    while True:
        p = b - ((f(b) * (b - a)) / (f(b) - f(a)))
        print(f'Iter: {i}. {p}')
        i += 1
        if abs(p - b) < epsilon:
            return round(p, 3)
        if i >=N:
            print("not convergent!")
            return
        a = b
        b = p

x = sp.symbols('x')
poly = [4, 0, -48, 5]
my_f = sp.cos(2*math.e**-2*x) / x**2+5*x+6
print("Polynomial: ", my_f)
my_f1 = sp.diff(my_f, x)
start_point = -1.1
end_point = 0
bigRange = (start_point, end_point)
print("Range: ", bigRange)
f = lambda x: math.cos(2 * math.e ** (-2 * x)) / (x ** 2 + 5 * x + 6)
d_poly = deriv_poly(poly)
f_d = create_poly_func(d_poly)
m = (start_point + end_point) / 2
b = end_point - m
epsilon = 0.0001
checker = [1, 2, 3, 4]
option = 5
i = 1
answer = set()
while(option not in checker):
    try:
        option = int(input('Please choose a method for finding the roots:'
                   '\n1.Bisection method\n2.Newton raphson\n3.Secant method\n'))

        end = start_point + 0.1
        start = start_point

        if option == 1:
            while end <= end_point:
                answer.add(bisection_method(start, end, f, epsilon))
                print("-----------------------")
                start = end
                end += 0.1

        elif option == 2:
            while end <= end_point:
                answer.add(newton_raphson(start, end, f,  epsilon))
                print("-----------------------")
                start = end
                end += 0.1

        elif option == 3:
            while end <= end_point:
                anw = secant_method(start, end, f, epsilon)
                if anw != None and anw < end_point:
                    answer.add(anw)
                print("-----------------------")
                start = end
                end += 0.1



    except ValueError:
        print("Wrong input")

if None in answer:
    answer.remove(None)
print("Intersection points:", *answer)





