import random
A = set()
n = int(input("Nhập vào số phần tử của set A: "))
for i in range(n):
    a = random.randint(1,1000)
    A.add(a)
print(f"tập A là {A}")
print(f"phần tử lớn nhất của tập A là {max(A)}")
print(f"phần tử nhỏ nhất của tập A là {min(A)}")
print(f"tổng của các phần tử của A = {sum(A)}")