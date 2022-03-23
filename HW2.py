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
    if len(res[0])==1:
        print("Solution vector: ")
    else:
        print("Matrix being solved: ")
    for r in res:
        print(r)
    print('\n')
    save_mat(mat1)
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

    flag = -1
    saveZero =-1

    for row in range(len(mat1)):
        for col in range(len(mat1)):
            if mat1[col][row] == 0.0 and col == row:
                saveZero = col
            elif mat1[col][row] != 0.0 and col != row and saveZero!= -1:
                el_mat=elemReset(el_mat)
                temp = el_mat[saveZero]
                el_mat[saveZero] = el_mat[col]
                el_mat[col] = temp
                mat1 = matrix_mul(el_mat, mat1)
                X = matrix_mul(el_mat,X)
                saveZero = -1


    el_mat = elemReset(mat1)

    while check != mat1:  #while the matrix still not identity

        for row in range(len(mat1)):
            for col in range(len(mat1)):

                if col == row and mat1[row][col] != 1 and mat1[row][col] != 0:
                    el_mat[row][col] = float(1 / mat1[row][col])
                    mat1 = matrix_mul(el_mat, mat1)
                    X = matrix_mul(el_mat, X)
                    el_mat = elemReset(mat1)

                elif mat1[row][col] != 0.0 and col != row:
                    el_mat[row][col] = float(-mat1[row][col]/mat1[col][col])
                    mat1 = matrix_mul(el_mat, mat1)
                    X = matrix_mul(el_mat, X)
                    el_mat = elemReset(mat1)
    tempM = []
    for i in X:
        tempM.append(i[0])
    X = list(map(lambda x: round(x, 9), tempM))
    print('the solution vector is:', X)

def save_mat(mat1):
    """
    Function to copy and save all elementary matrices
    :param mat1: Matrix
    :return: None
    """
    global counter
    global cache
    if mat1 not in cache:
        cache.append(mat1)
        counter += 1
    else:
        return
    with open('elem_matrix.txt', 'a') as f:
        f.writelines("Elementary matrix number " + str(counter) + ":\n")
        for i in mat1:
            f.writelines(str(i))
            f.write('\n')
        f.write('\n')

# Driver
counter = 0
cache = []

X = [[1,17,3],
    [0,0,9],
    [0 ,1,61]]

Y = [[1,1,1,6],
    [1,2,5,-4],
    [2,5,-1,27]]

matrix(Y)

print('solved with', counter, 'elementary matrices')






