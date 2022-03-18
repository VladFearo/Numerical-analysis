def matrix_mul(mat1, mat2):
    """
    Function to multiply two matrices using nested loops
    :param mat1: matrix 1
    :param mat2: matrix 2
    :return: result matrix
    """
    global counter
    if len(mat1[0]) != len(mat2):
        print("Error")
        return
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
    for r in res:
        print(r)
    print('\n')
    save_mat(mat2)
    counter += 1
    return res

def elemReset(mat1):
    el_mat = []
    list1 = [0] * len(mat1)
    for i in range(len(mat1)):  # create matrix with only 0
        el_mat.append(list1.copy())

    for j in range(len(el_mat)):  # create identity matrix
        for k in range(len(el_mat)):
            if j == k:
                el_mat[j][k] = 1
    return el_mat


def matrix(mat1):
    el_mat = elemReset(mat1)
    check = elemReset(mat1)

    flag = -1
    checker = True

    """
    [[1,5,9],
    [0,0,3],
    [1 ,0,61]]
    """

    for i in range(len(mat1)):
        if mat1[i][0] == 0.0:
            flag = i
        elif flag != -1:
            temp = el_mat[flag]
            el_mat[flag] = el_mat[i]
            el_mat[i] = temp
            break

    if flag == len(mat1) - 1:
        print("There is no solution for this matrix")
        return

    if flag != -1:
        mat1 = matrix_mul(el_mat, mat1)

    while check != mat1:  #while the matrix still not identity

        for col in range(len(mat1)):
            for row in range(len(mat1)):
                if col == row and mat1[col][row] != 1:
                    el_mat[col][row] = float(1 / mat1[col][row])
                    mat1 = matrix_mul(mat1, el_mat)
                    el_mat = elemReset(mat1)

                elif mat1[col][row] != 0.0 and col != row:
                    el_mat[col][row] = float(-mat1[col][row])
                    mat1 = matrix_mul(mat1, el_mat)
                    el_mat = elemReset(mat1)


def save_mat(mat1):
    with open('elem_matrix.txt','a') as f:
        for i in mat1:
            f.writelines(str(i))
            f.write('\n')
        f.write('\n')


counter = 0


X = [[1,5,9],
    [0,0,3],
    [1 ,0,61]]



matrix(X)
print('used with', counter, 'elementary matrix')

Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]






