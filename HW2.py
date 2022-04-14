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
   # if len(res[0]) > 1:
    #    for i in range(len(mat1)):
     #       if i == 1:
      #          print(list(map(lambda x: round(x, 2), mat1[i])), ' * ', list(map(lambda x: round(x, 2), mat2[i])),' =\t', list(map(lambda x: round(x, 2), res[i])))
       #     else:
        #        print(list(map(lambda x: round(x, 2), mat1[i])), '   ', list(map(lambda x: round(x, 2), mat2[i])),'   \t\t', list(map(lambda x: round(x, 2), res[i])))
    #print('\n')
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
    saveZero = -1
    mat1, X = biggest_pivot(mat1, X)
    for row in range(len(mat1)):
        for col in range(len(mat1)):
            if mat1[col][row] == 0.0 and col == row:
                saveZero = col
            elif mat1[col][row] != 0.0 and col != row and saveZero!= -1:
                el_mat = elemReset(el_mat)
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
    X = list(map(lambda x: round(x, 2), tempM))
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
                for this_row in range(row , len(mat)):
                    if mat[this_row][col] > biggest:
                        biggest_row = this_row
                        biggest = mat[this_row][col]
                el_mat = elemReset(mat)
                temp = el_mat[row]
                el_mat[row] = el_mat[biggest_row]
                el_mat[biggest_row] = temp
                mat = matrix_mul(el_mat, mat)
                X = matrix_mul(el_mat, X)
    print('matrix after max pivot:')
    for x in mat:
        print(x)
    print('\n')
    return mat, X


# Driver
counter = 0
cache = []



Y = [[1,0,-1,0.2],
    [-0.5,1,-0.25,-1.425],
    [1,-0.5,1,2]]

#matrix(Y)


#print('solved with', counter, 'elementary matrices')






