m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))
A = []
for i in range(m):
    dong = []
    for j in range(n):
        phan_tu = int(input(f"Nhập phần tử A[{i+1},{j+1}]: "))
        dong.append(phan_tu)
    A.append(dong)
print("Ma trận A là:")
for dong in A:
    print(dong)
tong = 0
for dong in A:
    for phan_tu in dong:
        tong += phan_tu
print("Tổng các phần tử của ma trận A là:", tong)
