import newton_raphson
import secant_method
import bisection_method


def deriv_poly(poly):
    """
    derives a polynomial list (e.g. [1,2,3] -> x^2+2x+3
    :param poly: a list of numbers representing a function
    :return: a list of numbers representing a function after derivation
    """
    deriv = []
    n = len(poly)
    for x in poly:
        if x != 0:
            n -= 1
            deriv.append(x * n)
        else:
            n -= 1
    return deriv


def print_poly(poly1, derive_poly=0):
    """
    prints a list repressenting a polynomial function in the form of a1x^n+a2x^n-1...an+1
    :param poly: a list repressenting a polynomail function
    :return: None
    """
    string = ''
    if derive_poly != 0:
        n = len(poly) - 1
    else:
        n = len(poly1)

    for x in range(len(poly1) - 1):
        if poly1[x] != 0:

            if derive_poly != 0 and n == 2:
                if poly1[x] == 1:
                    string += f'x'
                else:
                    string += f'{poly1[x]}x'
                    if poly1[x + 1] > 0:
                        string += "+"

                    if poly[x + 1] != 0:
                        string += f'{poly1[x + 1]}'
                        break

            if n == 0:
                if poly[x] > 0:
                    string += f'{poly1[x]}'
                else:
                    string += f'({poly1[x]})'
            elif poly1[x] == 1:

                if n > 2:
                    string += f'x^{n - 1}'
                if n == 2:
                    string += f'x'
                if n == 1:
                    string += f'1'

            elif n == 1:
                string += f'{poly1[x]}'
            else:
                string += f'{poly1[x]}x^{n - 1}'
        # else:
        #     n -= 1
        n -= 1
        if n > 0 and poly1[x + 1] > 0:
            string += '+'

    print(string)


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
            solution += poly * (x ** n)
            n -= 1
        return solution

    return func


def poly_print(poly, deriv_poly):
    print("Polynomial")
    print_poly(poly)
    print("Derivative of polynomial")
    print_poly(d_poly, len(poly))


poly = [4, 0, -48, 5]
start_point = (float)(input("Enter start point\t"))
end_point = (float)(input("Enter end point\t"))
bigRange = (start_point, end_point)
print(bigRange)
epsilon = 0.0001
option = int(input('Please choose a method for finding the roots:'
                   '\n1.Bisection method\n2.Newton raphson\n3.Secant method\n'))
section = float(input('Please enter the section length'))
f = create_poly_func(poly)
d_poly = deriv_poly(poly)
f_d = create_poly_func(d_poly)
poly_print(poly, d_poly)
m = (start_point + end_point) / 2
b = end_point - m
print("m =", m, "\nb =", b)
while (f(start_point) > 0 and f(end_point) > 0) or (f(start_point) < 0 and f(end_point) < 0):
    f(start_point)


if option == 1:
    print("Intersection point:", bisection_method.bisection_method(-3, 2, f))
    print("Intersection point:", bisection_method.bisection_method(-3, 2, f_d))
elif option == 2:
    print(newton_raphson.newton_raphson(3, 4, f, f_d, epsilon))
elif option == 3:
    print("Answer: ", secant_method.secant_method(3, 4, f, epsilon))
