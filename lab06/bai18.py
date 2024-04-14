m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))

A = []

print("Nhập các phần tử của ma trận A:")
for i in range(m):
    row = []
    for j in range(n):
        phan_tu = int(input(f"Nhập phần tử a{i+1}{j+1}: "))
        row.append(phan_tu)
    A.append(row)

tong = sum(sum(row) for row in A)

print("Ma trận A:")
for row in A:
    print(row)
print("Tổng các phần tử của ma trận A:", tong)
