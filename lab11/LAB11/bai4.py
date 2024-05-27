# Hàm để nhập mảng hai chiều từ bàn phím
def nhap_mang(m, n):
    A = []
    for i in range(m):
        row = list(map(float, input(f"Nhập hàng thứ {i + 1}: ").split()))
        A.append(row)
    return A

# Hàm để tìm giá trị lớn nhất và nhỏ nhất trên mỗi cột
def tim_gia_tri_tren_cot(A, m, n):
    max_in_columns = [-float('inf')] * n
    min_in_columns = [float('inf')] * n

    for j in range(n):
        for i in range(m):
            if A[i][j] > max_in_columns[j]:
                max_in_columns[j] = A[i][j]
            if A[i][j] < min_in_columns[j]:
                min_in_columns[j] = A[i][j]

    return max_in_columns, min_in_columns

# Hàm để tìm giá trị lớn nhất và nhỏ nhất của mảng A cùng các chỉ số hàng và cột của 2 phần tử này
def tim_gia_tri_cua_mang(A, m, n):
    max_value = -float('inf')
    min_value = float('inf')
    max_index = (0, 0)
    min_index = (0, 0)

    for i in range(m):
        for j in range(n):
            if A[i][j] > max_value:
                max_value = A[i][j]
                max_index = (i, j)
            if A[i][j] < min_value:
                min_value = A[i][j]
                min_index = (i, j)

    return max_value, min_value, max_index, min_index

# Chương trình chính
m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))

A = nhap_mang(m, n)

# a. Tìm giá trị lớn nhất và nhỏ nhất trên mỗi cột
max_in_columns, min_in_columns = tim_gia_tri_tren_cot(A, m, n)
print("Giá trị lớn nhất trên mỗi cột:", max_in_columns)
print("Giá trị nhỏ nhất trên mỗi cột:", min_in_columns)

# b. Tìm giá trị lớn nhất và phần tử nhỏ nhất của mảng A cùng các chỉ số hàng và cột của 2 phần tử này
max_value, min_value, max_index, min_index = tim_gia_tri_cua_mang(A, m, n)
print("Giá trị lớn nhất của mảng A:", max_value, "tại chỉ số:", max_index)
print("Giá trị nhỏ nhất của mảng A:", min_value, "tại chỉ số:", min_index)