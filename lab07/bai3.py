import random
n=int(input("nhap so so thuc muon nhap: "))
A=set(random.choices(range(-100000,100000),k=n))
print(A)
max=0
for i in A:
    if max<i:
        max=i
print(max)

min=0
for i in A:
    if i < min:
        min=i
print(min)

tong=0
for i in A:
    tong+=i
print(tong)