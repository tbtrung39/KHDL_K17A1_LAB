import random
gioi_han=int(input("Nhập A Và B giới hạn lấy ngẫu nhiên:"))
A=set()
B=set()
A_1=random.randint(1,gioi_han)
B_1=random.randint(1,gioi_han)

for i in range(A_1):
    A.add(random.randint(1,gioi_han))
print(A)
for j in range(A_1):
    B.add(random.randint(1,gioi_han))
print(B)
tap_chug=A.intersection(B)
print(tap_chug)
