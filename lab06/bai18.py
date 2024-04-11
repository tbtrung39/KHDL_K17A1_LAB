m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))
A = []
for i in range(m):
    row = []
    for j in range(n):
        num = int(input(f"Nhập phần tử a{i+1}{j+1}: "))
        row.append(num)
    A.append(row)
tong= sum(sum(row) for row in A)
print("Ma trận A:")
for row in A:
    print(row)
print("Tổng các phần tử của ma trận A:", tong)
