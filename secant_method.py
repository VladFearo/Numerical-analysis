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
    while True:
        p = b - ((f(b) * (b - a)) / (f(b) - f(a)))
        print(f'Iter: {i}. {p}')
        i += 1
        if abs(p - b) < epsilon:
            return p
        a = b
        b = p