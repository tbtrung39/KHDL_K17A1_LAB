m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))
A = []
print("Nhập các phần tử của ma trận:")
for i in range(m):
    hang_ngang = []
    for j in range(n):
        aij = int(input(f"Nhập phần tử a{i+1}{j+1}: "))
        hang_ngang.append(aij)
    A.append(hang_ngang)
tong = 0
for hang_ngang in A:
    tong += sum(hang_ngang)
print("Ma trận A:", A)
print("Tổng các phần tử của ma trận A:", tong)
