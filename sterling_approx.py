import math


def sterling_approximation(n):
    """
    an approximation of calculation the factorial of a number
    :param n: a number
    :return: the approximation
    """
    return (n**n)*(math.e**(-n))*math.sqrt(n)*math.sqrt(2*math.pi)


