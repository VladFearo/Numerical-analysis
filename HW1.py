print(abs(3.0 * (4.0 / 3.0 - 1) - 1))  # without round function we get an incorrect answer which is the machine epsilon.
# prints: 2.220446049250313e-16

print(round(abs(3.0 * (4.0 / 3.0 - 1) - 1)))  # round function rounds to the nearest number and removes the imprecision
# prints: 0


def epsilon_find():
    """
    searches for the lowest number s.t. 1 - (1 + epsilon) = 0 epsilon being the precision of the machine
    :return: a float number that is the epsilon
    """
    epsilon = 1.0
    while (1.0 + 0.5 * epsilon) != 1.0:
        epsilon = 0.5 * epsilon
    return epsilon


print(epsilon_find())   # prints 2.220446049250313e-16
