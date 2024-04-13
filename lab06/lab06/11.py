import random
n = int(input("Nhập số phần tử của danh sách A: "))
A = [int(input(f"Nhập phần tử thứ {i+1} của danh sách A: ")) for i in range(n)]
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("Danh sách B chứa các phần tử chia hết cho 3 nhưng không chia hết cho 5:",B)
C = [x**2 for x in A]
print("Danh sách C chứa bình phương của các phần tử trong danh sách A:",C)
D = random.sample(A, k=min(5, len(A)))
print("Danh sách D gồm các phần tử được chọn ngẫu nhiên từ danh sách A:",D)

