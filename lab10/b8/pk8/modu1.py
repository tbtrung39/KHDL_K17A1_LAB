def nhap_matran(size):
    matrix = []
    print("Nhập ma trận {}x{}:".format(size, size))
    for i in range(size):
        row = []
        for j in range(size):
            row.append(int(input("Nhập phần tử tại hàng {} cột {}: ".format(i + 1, j + 1))))
        matrix.append(row)
    return matrix

def in_matran(matrix):
    print("Ma trận {}x{}:".format(len(matrix), len(matrix)))
    for row in matrix:
        print(row)

def chuyen_vi(matrix):
    transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))]
    print("Ma trận chuyển vị:")
    for row in transposed_matrix:
        print(row)

def kiem_tra_doi_xung(matrix):
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True
