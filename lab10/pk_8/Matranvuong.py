def nhap_matran():
    N = int(input("Nhập kích thước của ma trận (NxN): "))
    print("Nhập dữ liệu cho ma trận:")
    matrix = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(int(input(f"Nhập phần tử [{i+1},{j+1}]: ")))
        matrix.append(row)
    return matrix

def in_matran(matrix):
    print("Ma trận:")
    for row in matrix:
        print(row)

def chuyen_vi(matrix):
    a = []
    for i in range(len(matrix)):
        b = []
        for j in range(len(matrix)):
            b.append(matrix[j][i])
        a.append(b)
    print("Ma trận chuyển vị:")
    for row in a:
        print(row)

def kiem_tra_doi_xung(matrix):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True
