import random

# Nhập số lượng phần tử của danh sách A từ bàn phffím
n = int(input("Nhập số lượng phần tử của danh sách A: "))

# Nhập các phần tử của danh sách A từ bàn phím
A = [int(input(f"Nhập phần tử thứ {i+1} của danh sách A: ")) for i in range(n)]

# Tạo danh sách B chứa các phần tử chia hết cho 3 nhưng không chia hết cho 5
B = [x for x in A if x % 3 == 0 and x % 5 != 0]

# Tạo danh sách C chứa các phần tử là bình phương của danh sách A
C = [x**2 for x in A]
# Tạo danh sách D gồm các phần tử lấy ngẫu nhiên từ danh sách A
D = random.sample(A, len(A))
print("Danh sách A:", A)
print("Danh sách B:", B)
print("Danh sách C:", C)
print("Danh sách D:", D)
