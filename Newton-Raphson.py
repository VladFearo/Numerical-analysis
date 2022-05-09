def print_poly(poly1, derive_poly = 0):
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

    for x in range(len(poly1)):
        if poly1[x] != 0:

            if derive_poly != 0 and n == 2:
                if poly1[x] == 1:
                    string += f'x'
                else:
                    string += f'{poly1[x]}x'
                    if poly1[x+1] > 0 :
                        string += "+"

                    if poly[x+1] != 0:
                        string += f'{poly1[x+1]}'
                        break

            if n == 0:
                if poly[x] > 0:
                    string += f'{poly1[x]}'
                else:
                    string += f'({poly1[x]})'
            elif poly1[x] == 1:

                if n > 2:
                    string += f'x^{n-1}'
                if n == 2:
                    string += f'x'
                if n == 1:
                    string += f'1'

            elif n == 1:
                string += f'{poly1[x]}'
            else:
                string += f'{poly1[x]}x^{n-1}'
        # else:
        #     n -= 1
        n -= 1
        if n > 0 and poly1[x+1] > 0:
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
            solution += poly*(x**n)
            n -= 1
        return solution
    return func

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

def newton_raphson(a, b, f):
    print("test a", f(a))
    print("test b", f(b))
    x1 = x0 - f(x0)
    return 0


poly = [4, 0, -48, 5]
f = create_poly_func(poly)
d_poly = deriv_poly(poly)
#f_d = create_poly_func(d_poly)

print("Polynomial")
print_poly(poly)
print("Derivative of polynomial")
print_poly(d_poly)
print(newton_raphson(2,3,f))