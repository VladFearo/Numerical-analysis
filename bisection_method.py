def deriv_poly(poly):
    """
    derives a polynomial list (e.g. [1,2,3] -> x^2+2x+3
    :param poly: a list of numbers representing a function
    :return: a list of numbers representing a function after derivation
    """
    deriv = []
    n = len(poly)
    for x in poly:
        if x!=0:
            n -= 1
            deriv.append(x * n)
        else:
            n-=1
    return deriv



def create_poly_func(f):
    """
    creates a python function repressenting a polynomial function
    :param f: a list repressenting a polynomial function
    :return: a python function repressenting a polynomial function
    """
    def func(x):
        n = len(f) - 1
        solution = 0
        for poly in f:
            solution += poly*(x**n)
            n -= 1
        return solution
    return func

def bisection_method(a, b, f):
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
            return bisection_method(a, m, f)
        elif f(m) * f(b) < 0:
            return bisection_method(m, b, f)
        else:
            i = 1

            return bisection_method(a,b,f_d)
    else:
        i = 1
        return round(m, 3)

i = 1