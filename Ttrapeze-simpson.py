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



def calcParts(f,a,b):
    max_f = sp.diff(f)  #first diff
    ans = solve(max_f)
    max_f = sp.diff(max_f)  #second diff
    max_f = lambdify(x, max_f)
    arr = []
    for i in ans:
        if max_f(i) < 0:
            arr.append(max_f(i))

    numerator = abs(((b - a)**3) * max(arr))
    denomiator = 12*epsilon
    n = math.sqrt(numerator / denomiator)
    return round(n)

#def partToSimpson(f,a,b):



def simpson( a, b):
    n = 10
    func = lambdify(x, f)
    h = (b-a) / n
    calc = func(a) + func(b)
    A = a + h
    for i in range(1,n):
        if i % 2 == 0:
            calc += 2*func(A)
        else:
            calc += 4*func(A)
        A += h
    calc *= (1/3) * h
    max_f = sp.diff(f)
    ans = solve(max_f)
    arr = []
    for i in range (0,3):
        max_f = sp.diff(max_f)
    if max_f == 0:
        max_f = 1
        arr.append(1)

    max_f = lambdify(x, max_f)
    for i in ans:
        if max_f(i) < 0:
            arr.append(max_f(i))

    E = ((h**4) / 90) * (b - a) * (max_f(max(arr)) / 2)
    return calc, E


x = sp.symbols('x')
f = 4*x**3 - 48*x + 5
epsilon = 0.000002
print("Area in trapeze method:",trapeze(f,0, math.pi),"Error range:",epsilon)
tup = simpson(0, math.pi)
print("Area in simpson method:",tup[0], "  Error range:",tup[1])

