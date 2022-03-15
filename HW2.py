def matrix_mul(mat1, mat2):
    """
    Function to multiply two matrices using nested loops
    :param mat1: matrix 1
    :param mat2: matrix 2
    :return: result matrix
    """
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



def matrix(mat1):
    el_mat = []
    List = [0] * len(mat1)
    for i in range(len(mat1)):
        el_mat.append(List.copy())

    for j in range(len(el_mat)):
        for k in range(len(el_mat)):
            if j == k:
                el_mat[j][k] = 1
    i = 0
    flag = -1
    temp = []
    j = 0
    while j <= len(mat1):
        if mat1[i][0] == 0.0:
            flag = i
            i += 1
        elif flag != -1:
            # save the matrix
            temp = el_mat[flag]
            el_mat[flag] = el_mat[i]
            el_mat[i] = temp
        j += 1

    save_mat(el_mat)
    matrix_mul(el_mat, mat1)


def save_mat(mat1):
    with open('elem_matrix.txt','w') as f:
        for i in mat1:
            f.writelines(str(i))
            f.write('\n')
        f.write('\n')





X = [[0,7,3],
    [1 ,5,6],
    [7 ,8,9]]

matrix(X)

Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]






