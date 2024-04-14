import random

n = int(input("Nhập số nguyên dương n: "))
A = [int(input(f"Nhập phần tử thứ {i+1} của danh sách A: ")) for i in range(n)]

B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("Danh sách B:", B)

C = [x**2 for x in A]
print("Danh sách C:", C)

D = random.choices([x for x in A if x % 3 == 0], k=random.randint(1, len(A)))
print("Danh sách D:", D)
