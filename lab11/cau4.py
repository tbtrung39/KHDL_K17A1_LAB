#nhập mảng hai chiều từ bàn phím
def nhap_mang(m, n):
    A = []
    for i in range(m):
        dong = list(map(float, input(f"Nhập hàng thứ {i + 1}: ").split()))
        A.append(dong)
    return A

#Tìm giá trị lớn nhất và nhỏ nhất trên mỗi cột
def gia_tri_tren_cot(A, m, n):
    lon_nhat_cot = [-float('inf')] * n
    nho_nhat_cot = [float('inf')] * n

    for j in range(n):
        for i in range(m):
            if A[i][j] > lon_nhat_cot[j]:
                lon_nhat_cot[j] = A[i][j]
            if A[i][j] < nho_nhat_cot[j]:
                nho_nhat_cot[j] = A[i][j]

    return lon_nhat_cot, nho_nhat_cot

#tìm giá trị lớn nhất và nhỏ nhất của mảng A cùng các chỉ số hàng và cột của 2 phần tử 
def gia_tri_cua_mang(A, m, n):
    gia_tri_lon_nhat = -float('inf')
    gia_tri_nho_nhat = float('inf')
    toi_da = (0, 0)
    toi_thieu = (0, 0)

    for i in range(m):
        for j in range(n):
            if A[i][j] > gia_tri_lon_nhat:
                gia_tri_lon_nhat = A[i][j]
                toi_da = (i, j)
            if A[i][j] < gia_tri_nho_nhat:
                gia_tri_nho_nhat = A[i][j]
                toi_thieu = (i, j)

    return gia_tri_lon_nhat, gia_tri_nho_nhat, toi_da, toi_thieu

m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))

A = nhap_mang(m, n)

# a. Tìm giá trị lớn nhất và nhỏ nhất trên mỗi cột
lon_nhat_cot, nho_nhat_cot = gia_tri_tren_cot(A, m, n)
print("Giá trị lớn nhất trên mỗi cột:", lon_nhat_cot)
print("Giá trị nhỏ nhất trên mỗi cột:", nho_nhat_cot)

# b. Tìm giá trị lớn nhất và phần tử nhỏ nhất của mảng A cùng các chỉ số hàng và cột của 2 phần tử này
gia_tri_lon_nhat, gia_tri_nho_nhat, toi_da, toi_thieu = gia_tri_cua_mang(A, m, n)
print("Giá trị lớn nhất của mảng A:", gia_tri_lon_nhat, "tại chỉ số:", toi_da)
print("Giá trị nhỏ nhất của mảng A:", gia_tri_nho_nhat, "tại chỉ số:", toi_thieu)