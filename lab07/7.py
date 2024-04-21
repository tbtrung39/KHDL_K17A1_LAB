import random
A=set()
B=set()
n=int(input("nhập số lượng phần tử tập hợp A : "))
m=int(input("nhập số lượng phần tử tập hợp B : "))
for i in range(n):
    A.add(random.choice("abcdefghijklmnopqrstuvwxyz0123456789"))
for i in range(m):
    B.add(random.choice("abcdefghijklmnopqrstuvwxyz0123456789"))
c=A.intersection(B)
print(c)