import sympy as sp
import math
from sympy import solve
from sympy.utilities.lambdify import lambdify


def trapeze(f, a, b):
    n = calcParts(f, a, b)
    B = (b - a) / n
    jumps = B
    calc = 0
    f = lambdify(x, f)
    for i in range(n):
        calc += 0.5 * (B - a) * (f(a) + f(B))
        a = B
        B += jumps
    return calc


def calcParts(f, a, b):
    max_f = sp.diff(f)  # first diff
    ans = solve(max_f)
    max_f = sp.diff(max_f)  # second diff
    max_f = lambdify(x, max_f)
    arr = []
    for i in ans:
        if max_f(i) < 0:
            arr.append(max_f(i))

    numerator = abs(((b - a) ** 3) * max(arr))
    denomiator = 12 * epsilon
    n = math.sqrt(numerator / denomiator)
    return round(n)


# def partToSimpson(f,a,b):


def simpson(a, b):
    n = 100
    print("number of slices picked:",n)
    func = lambdify(x, f)
    h = (b - a) / n
    calc = func(a) + func(b)
    calc_str = f'integral: 1/3*{h}('
    A = a + h
    for i in range(1, n):
        if i % 2 == 0:
            calc += 2 * func(A)
            calc_str += f'2*f({A})'
        else:
            calc += 4 * func(A)
            calc_str += f'4*f({A})'

        A += h

    calc *= (1 / 3) * h
    calc_str += ')'
    print(calc_str)
    print(f' 1/3*{h}*(', calc, ')')
    return calc


x = sp.symbols('x')
f = sp.cos(2 * math.e ** (-2 * x)) / (x ** 2 + 5 * x + 6)
epsilon = 0.000001
# print("Area in trapeze method:",trapeze(f,-0.4, 0.4),"Error range:",epsilon)
tup = simpson(a=-0.4, b=0.4)
print("Area in simpson method:", tup)
