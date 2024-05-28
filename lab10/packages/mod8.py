def input_matrix():
    M = int(input("Nhập số hàng của ma trận (M): "))
    N = int(input("Nhập số cột của ma trận (N): "))    
    matrix = []
    print("Nhập các phần tử của ma trận:")
    for i in range(M):
        row = list(map(int, input().split()))
        matrix.append(row)    
    return matrix, M, N
def transpose_matrix(matrix, M, N):
    transposed = [[matrix[j][i] for j in range(M)] for i in range(N)]
    return transposed
def is_symmetric(matrix, M, N):
    if M != N:
        return False
    for i in range(M):
        for j in range(N):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))