from HW2 import biggest_pivot

a = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
b = [[2], [6], [5]]
epsilon = 0.00001


def gs_calculations(mat, sol):
    xn, yn, zn = 0, 0, 0
    counter = 1
    print('__________________________')
    print("gauss-seidel method:")

    if mat[0][0] == 0 or mat[1][1] == 0 or mat[2][2] == 0:
        print('__________________________')
        print("there is no solution")
    else:

        while True:
            print(f'Iteration number {counter}:')
            print(f'{xn=} {yn=} {zn=}')
            prev_xn, prev_yn, prev_zn = xn, yn, zn
            xn = (sol[0][0] - mat[0][1] * yn - mat[0][2] * zn) / mat[0][0]
            yn = (sol[1][0] - mat[1][0] * xn - mat[1][2] * zn) / mat[1][1]
            zn = (sol[2][0] - mat[2][0] * xn - mat[2][1] * yn) / mat[2][2]
            counter += 1
            if abs(xn - prev_xn) < epsilon and abs(yn - prev_yn) < epsilon and abs(zn - prev_zn) < epsilon:
                print('__________________________')
                print(f'Calculated with {counter-1} iterations')
                print('The solution vector is: ')
                return list(map(lambda y: round(y, 8), [xn, yn, zn]))
            elif counter >= 100:
                print('__________________________')
                print("there is no solution")


def gauss_seidel(mat, sol):
    if dominant_pivot(mat):
        return gs_calculations(mat, sol)
    else:
        big_mat, big_sol = biggest_pivot(mat, sol)
        if dominant_pivot(big_mat):
            return gs_calculations(big_mat, big_sol)
        else:
            print("There is no dominant pivot")
            return gs_calculations(big_mat, big_sol)


def jacobi(mat, sol):
    if dominant_pivot(mat):
        return j_calculations(mat, sol)
    else:
        big_mat, big_sol = biggest_pivot(mat, sol)
        if dominant_pivot(big_mat):
            return j_calculations(big_mat, big_sol)
        else:
            print("There is no dominant pivot")
            return j_calculations(big_mat, big_sol)


def j_calculations(mat, sol):
    xn, yn, zn = 0, 0, 0
    counter = 1
    print('__________________________')
    print("jacobi method:")
    if mat[0][0] == 0 or mat[1][1] == 0 or mat[2][2] == 0:
        print('__________________________')
        print("there is no solution")
    else:

        while True:
            print(f'Iteration number {counter}:')
            print(f'{xn=} {yn=} {zn=}')
            next_xn = (sol[0][0] - mat[0][1] * yn - mat[0][2] * zn) / mat[0][0]
            next_yn = (sol[1][0] - mat[1][0] * xn - mat[1][2] * zn) / mat[1][1]
            next_zn = (sol[2][0] - mat[2][0] * xn - mat[2][1] * yn) / mat[2][2]
            counter += 1
            if abs(xn - next_xn) < epsilon and abs(yn - next_yn) < epsilon and abs(zn - next_zn) < epsilon:
                print('__________________________')
                print(f'Calculated with {counter-1} iterations')
                print(f'The solution vector is: ')
                return list(map(lambda y: round(y, 8), [xn, yn, zn]))
            elif counter >= 100:
                print('__________________________')
                print("there is no solution")
            xn, yn, zn = next_xn, next_yn, next_zn



def dominant_pivot(matrix):
    j = 0
    counter = 0
    for i in matrix:
        abs_list = list(map(abs, i))
        if i[j] > sum(abs_list) - abs(i[j]):
            counter += 1
        j += 1
    return counter == len(matrix)
while True:
    choice = input("Choose an option for calculations: \n1.gauss-seidel\n2.jacobi\n")
    if choice == '1':
        print(gauss_seidel(a, b))
        break;
    elif choice == '2':
        print(jacobi(a, b))
        break;
    else:
        print("wrong input try again")
