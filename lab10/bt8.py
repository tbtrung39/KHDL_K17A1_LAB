from packages import transpose_matrix,is_symmetric,print_matrix,input_matrix
matrix, M, N = input_matrix()
transposed = transpose_matrix(matrix, M, N)
symmetric = is_symmetric(matrix, M, N)
print("Ma trận gốc:")
print_matrix(matrix)
print("Ma trận chuyển vị:")
print_matrix(transposed)
if symmetric:
    print("Ma trận là ma trận đối xứng.")
else:
    print("Ma trận không phải là ma trận đối xứng.")