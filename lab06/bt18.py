# Nhập số hàng và số cột của ma trận
m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))

# Khởi tạo ma trận A với các phần tử nhập từ người dùng
A = []
for i in range(m):
    hang = []
    for j in range(n):
        phan_tu = int(input(f"Nhập phần tử A[{i+1},{j+1}]: "))
        hang.append(phan_tu)
    A.append(hang)

# In ma trận A
print("Ma trận A:")
for hang in A:
    print(hang)

# Tính tổng các phần tử của ma trận A
tong = sum(sum(hang) for hang in A)

# In tổng các phần tử của ma trận A
print("Tổng các phần tử của ma trận A:", tong)
