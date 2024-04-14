m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))
A = []
for i in range(m):
    hang = []
    for j in range(n):
        phan_tu = int(input(f"Nhập phần tử A[{i+1},{j+1}]: "))
        hang.append(phan_tu)
    A.append(hang)

print("Ma trận A:")
for hang in A:
    print(hang)
tong = sum(sum(hang) for hang in A)
print("Tổng các phần tử của ma trận A:", tong)
