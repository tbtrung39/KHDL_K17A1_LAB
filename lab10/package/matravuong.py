def Ma_tran_vuong(n):
    ma_tran = []
    for _ in range(n):
        dong = []
        for _ in range(n):
            gia_tri = int(input("Nhập giá trị: "))
            dong.append(gia_tri)
        ma_tran.append(dong)
    return ma_tran

def Ma_tran_chuyen_vi(ma_tran):
    dong = len(ma_tran)
    cot = len(ma_tran[0])
    ma_tran_chuyen_vi = [[0 for _ in range(dong)] for _ in range(cot)]
    
    for i in range(dong):
        for j in range(cot):
            ma_tran_chuyen_vi[j][i] = ma_tran[i][j]
    
    return ma_tran_chuyen_vi

def doi_xung(ma_tran):
    dong = len(ma_tran)
    cot = len(ma_tran[0])
    
    if dong != cot:
        return False
    
    for i in range(dong):
        for j in range(cot):
            if ma_tran[i][j] != ma_tran[j][i]:
                return False
    
    return True

# Example usage
n = int(input("Nhập kích thước ma trận vuông: "))
matrix = Ma_tran_vuong(n)
print("Ma trận vừa nhập:")
for row in matrix:
    print(row)

transpose_matrix = Ma_tran_chuyen_vi(matrix)
print("Ma trận chuyển vị:")
for row in transpose_matrix:
    print(row)

if doi_xung(matrix):
    print("Ma trận là ma trận đối xứng.")
else:
    print("Ma trận không phải là ma trận đối xứng.")