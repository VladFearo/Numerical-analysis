import math


def matrix_mul(mat1, mat2):
    """
    Function to multiply two matrices using nested loops
    :param mat1: Matrix 1
    :param mat2: Matrix 2
    :return: Result matrix
    """
    result = []
    res = []
    temp = []
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                temp.append(mat1[i][k] * mat2[k][j])
            result.append(sum(temp))
            temp.clear()
        temp2 = result.copy()
        res.append(temp2)
        result.clear()
    """if len(res[0]) > 1:
        for i in range(len(mat1)):
            if i == 1:
                print(list(map(lambda x: round(x, 2), mat1[i])), ' * ', list(map(lambda x: round(x, 2), mat2[i])),' =\t', list(map(lambda x: round(x, 2), res[i])))
            else:
                print(list(map(lambda x: round(x, 2), mat1[i])), '   ', list(map(lambda x: round(x, 2), mat2[i])),'   \t\t', list(map(lambda x: round(x, 2), res[i])))
    print('\n')"""
    return res


def elemReset(mat1):
    """
    Function to crate and initialize elementary matrices
    :param mat1: Matrix
    :return: Elementary matrix
    """
    el_mat = []
    list1 = [0] * len(mat1[0])
    for i in range(len(mat1[0])):  # create matrix with only 0
        el_mat.append(list1.copy())

    for j in range(len(el_mat[0])):  # create identity matrix
        for k in range(len(el_mat[0])):
            if j == k:
                el_mat[j][k] = 1
    return el_mat


def matrix(mat1):
    """
    Function to find a solution based on the given matrix
    using the elementary method
    :param mat1: Matrix
    :return: None (print only)
    """
    X = []
    for i in mat1:
        X.append([i.pop(-1)])

    el_mat = elemReset(mat1)
    check = elemReset(mat1)
    saveZero = -1
    mat1, X = biggest_pivot(mat1, X)
    for row in range(len(mat1)):
        for col in range(len(mat1)):
            if mat1[col][row] == 0.0 and col == row:
                saveZero = col
            elif mat1[col][row] != 0.0 and col != row and saveZero != -1:
                el_mat = elemReset(el_mat)
                temp = el_mat[saveZero]
                el_mat[saveZero] = el_mat[col]
                el_mat[col] = temp
                mat1 = matrix_mul(el_mat, mat1)
                X = matrix_mul(el_mat, X)
                saveZero = -1

    el_mat = elemReset(mat1)

    while check != mat1:  # while the matrix still not identity

        for row in range(len(mat1)):
            for col in range(len(mat1)):

                if col == row and mat1[row][col] != 1 and mat1[row][col] != 0:
                    el_mat[row][col] = float(1 / mat1[row][col])
                    mat1 = matrix_mul(el_mat, mat1)
                    X = matrix_mul(el_mat, X)
                    el_mat = elemReset(mat1)

                elif mat1[row][col] != 0.0 and col != row:
                    el_mat[row][col] = float(-mat1[row][col] / mat1[col][col])
                    mat1 = matrix_mul(el_mat, mat1)
                    X = matrix_mul(el_mat, X)
                    el_mat = elemReset(mat1)
    tempM = []
    for i in X:
        tempM.append(i[0])
    # X = list(map(lambda x: round(x, 2), tempM))
    # print('the solution vector is:', *X)
    return X


def biggest_pivot(mat, X):
    """
        finds the max pivot on the matrix and changes lines using elementary matrcies
        :param mat: Matrix
        :param X: Solution vector
        :return: Matrix, solution vector
        """
    for row in range(len(mat)):

        for col in range(len(mat)):
            if col == row:
                biggest = mat[row][col]
                biggest_row = row
                for this_row in range(row, len(mat)):
                    if mat[this_row][col] > biggest:
                        biggest_row = this_row
                        biggest = mat[this_row][col]
                el_mat = elemReset(mat)
                temp = el_mat[row]
                el_mat[row] = el_mat[biggest_row]
                el_mat[biggest_row] = temp
                mat = matrix_mul(el_mat, mat)
                X = matrix_mul(el_mat, X)
    # print('matrix after max pivot:')
    # for x in mat:
    #    print(x)
    # print('\n')
    return mat, X


# Driver
counter = 0
cache = []


def linear(points, x):
    for i in range(len(points) - 1):
        if points[i][X_Value] < x < points[i + 1][X_Value]:
            x1, x2, y1, y2 = points[i][X_Value], points[i + 1][X_Value], points[i][Y_Value], points[i + 1][Y_Value]

    return (((y1 - y2) / (x1 - x2)) * x) + ((y2 * x1 - y1 * x2) / (x1 - x2))


def polynomial(points, x):
    mat = [[1, points[1][X_Value], points[1][X_Value] ** 2, points[1][Y_Value]],
           [1, points[2][X_Value], points[2][X_Value] ** 2, points[2][Y_Value]],
           [1, points[3][X_Value], points[3][X_Value] ** 2, points[3][Y_Value]]]
    print("matrix:")
    for _ in mat:
        print(mat)
    sol = matrix(mat)
    print(f'y={sol[0][0]} + {sol[1][0]}x + {sol[2][0]}x^2')
    return sol[0][0] + sol[1][0] * x + sol[2][0] * x ** 2


def lagrange_make(points, i, x):
    total = 1

    for j in range(len(points)):
        if i != j:
            total *= (x - points[j][X_Value]) / (points[i][X_Value] - points[j][X_Value])

    return total


def lagrange(points, x):
    total = 0
    for i in range(len(points)):
        total += lagrange_make(points, i, x) * points[i][Y_Value]

    return total


def neville_interpolation(points, xf):
    n = len(points)
    x = 0
    y = 1
    pointlist = []
    for i in points:
        pointlist.append(list(i))

    # pointslist = list(points)
    for i in range(1, n, +1):
        for j in range(n - 1, i - 1, -1):
            pointlist[j][y] = ((xf - pointlist[j - i][x]) * pointlist[j][y] - (xf - pointlist[j][x]) * pointlist[j - 1][
                y]) / (
                                      pointlist[j][x] - pointlist[j - i][x])
            print(pointlist[j][y])
    print(f'y=({xf}-{pointlist[j-1][x]})*{pointlist[j][y]}-({xf}-{pointlist[j][x]})*{pointlist[j - 1][y]}/({pointlist[j][x]}-{pointlist[j - i][x]}))')

    result = str(pointlist[n - 1][y])
    return result


def spline_nat(points, x):
    h = []
    lmbda = []
    lmbda.append(0)
    miu = []
    miu.append(0)  # was 1
    d = []
    d.append(0)
    mat = []
    temp = []
    counter = -1
    two = [2] * len(points)
    rotate = [miu, two, lmbda]
    for i in range(len(points) - 1):
        h.append(points[i + 1][X_Value] - points[i][X_Value])
    for i in range(1, len(points) - 1):
        lmbda.append(h[i] / (h[i] + h[i - 1]))
    for i in range(1, len(points) - 1):
        miu.append(1 - lmbda[i])
    for i in range(1, len(points) - 1):
        d.append((6 / (h[i - 1] + h[i])) *
                 (((points[i + 1][Y_Value] - points[i][Y_Value])
                   / h[i]) - ((points[i][Y_Value] - points[i - 1][Y_Value]) / h[i - 1])))
    for i in range(len(points)):
        for j in range(len(points)):
            temp.append(0)
        mat.append(temp)
        temp = []
    for i in range(len(points) - 1):
        for j in range(len(points) - 1):
            if j + counter < len(points):
                mat[i][j + counter] = rotate[j % 3][i]
        counter += 1
    for row in mat:
        row.pop(0), row.pop(-1)
    mat.pop(0), mat.pop(-1)
    # print(mat)
    sol_mat = []
    temp = []
    counter = 1
    for row in mat:
        for col in row:
            temp.append(col)
        temp.append(d[counter])
        sol_mat.append(temp)
        temp = []
        counter += 1
    sol_vector = matrix(sol_mat)
    temp = []
    for i in sol_vector:
        temp.append(i[0])
    sol_vector = temp
    sol_vector.append(0)

    for i in range(len(points) - 1):
        if points[i][X_Value] < x < points[i + 1][X_Value]:
            fract1 = (((points[i + 1][X_Value] - x) ** 3) * sol_vector[i - 1] + ((x - points[i][X_Value]) ** 3) *
                      sol_vector[i]) / 6 * h[i]
            fract2 = ((points[i + 1][X_Value] - x) * points[i][Y_Value] + (x - points[i][X_Value]) * points[i + 1][
                Y_Value]) / h[i]
            fract3 = ((points[i + 1][X_Value] - x) * sol_vector[i - 1] + ((x - points[i][X_Value]) * sol_vector[i]) * h[
                i]) / 6

    return fract1 + fract2 - fract3


# print(spline_nat(test_points, math.pi / 3))

points = [[0.35, -213.5991], [0.4, -204.4416], [0.55, -194.9375], [0.65, -185.0256], [0.7, -174.6711],
          [0.85, -163.8656], [0.9, -152.6271]]
X_Value = 0
Y_Value = 1
x = 0.75
test_points = [[0, 0], [math.pi / 6, 0.5], [math.pi / 4, 0.7072], [math.pi / 2, 1]]
option = 0
print("Table of dots", points, "\nx dot", x)
while True:
    try:
        option = int(input("\nPlease choose interpolation\n1.linear\n2.polinomial\n3.lagrange\n4.neville\n5.spline\n6"
                           ".exit\n "))
        if option == 1:
            print("y dot:", linear(points, x))

        if option == 2:
            print("y dot:", polynomial(points, x))

        if option == 3:
            print("y dot:", lagrange(points, x))

        if option == 4:
            print("y dot:", neville_interpolation(points, x))

        if option == 5:
            print("y dot:", spline_nat(test_points, x=math.pi / 3))

        if option == 6:
            break

    except ValueError:
        print("Wrong input")
