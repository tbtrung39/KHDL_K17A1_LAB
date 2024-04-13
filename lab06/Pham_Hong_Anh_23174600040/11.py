import random
n = int(input("Nhập số lượng phần tử n của danh sách A: "))
A = []
for i in range(n):
    so = int(input(f"Nhập phần tử thứ {i+1}: "))
    A.append(so)

# Tạo danh sách B chứa các phần tử chia hết cho 3 nhưng không chia hết cho 5 từ danh sách A
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("Danh sách B:", B)

# Tạo danh sách C với các phần tử là bình phương của các phần tử trong danh sách A
C = [x**2 for x in A]
print("Danh sách C:", C)

# Tạo danh sách D chứa các phần tử lấy ngẫu nhiên từ danh sách A mà chia hết cho 3
D = [random.choice([x for x in A if x % 3 == 0]) for _ in A if any(x % 3 == 0 for x in A)]
print("Danh sách D:", D)