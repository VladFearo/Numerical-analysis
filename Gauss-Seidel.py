import numpy as np

a = np.array(  # n x n matrix
    [[1,0,-1],
    [-0.5,1,-0.25,],
    [0,0,1,]])
b = np.array([0.2, -1.425, 2])  #solution vector

x = np.linalg.solve(a, b)  #matrix solution


def gauss_seidel(A, b):
    xn, yn, zn = 0, 0, 0
    counter = 1
    if dominant_pivot(A):
        while True:
            print(f'Iteration number {counter}:')
            print(f'{xn=} {yn=} {zn=}')
            xn = (b[0] - A[0][1] * yn - A[0][2] * zn) / A[0][0]
            yn = (b[1] - A[1][0] * xn - A[1][2] * zn) / A[1][1]
            zn = (b[2] - A[2][0] * xn - A[2][1] * yn) / A[2][2]
            counter += 1
            if xn == x[0] and yn == x[1] and zn == x[2]:
                print('__________________________')
                print(f'The solution vector is: ')
                print(list(map(lambda y: round(y, 8), [xn, yn, zn])))
                break


def dominant_pivot(matrix):
    j = 0
    for i in matrix:
        abs_list = list(map(abs, i))
        if i[j] < sum(abs_list) - abs(i[j]):
            print("Not a dominant pivot")
            return False
        j += 1
    return True


gauss_seidel(a, b)
