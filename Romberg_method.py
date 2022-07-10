import sympy as sp
import math
from sympy import solve
from sympy.utilities.lambdify import lambdify


def romberg(f,a,b,n):
    r = []
    h = (b - a )
    r.append([(h / 2.0)*(f(a) + f(b))])

    for i in range(1, n + 1):
        h = h / 2.
        sum = 0

        for k in range(1, 2**i, 2):
            sum = sum + f(a + k*h)


        rowi = [0.5*r[i-1][0] + sum*h]

        for j in range(1, i + 1):

            rij = rowi[j-1] + (rowi[j-1]-r[i-1][j-1]) / (4.**j-1.)
            rowi.append(rij)
        print(rowi)
        r.append(rowi)
    print("solution", rowi[len(rowi)-1])



x = sp.symbols('x')
f = sp.sin(x)
f = lambdify(x, f)
romberg(f,0,math.pi,5)