import random

n=int(input("Nhap so luong so thuc:"))

a = set()

for _ in range(n):
    a.add(random.uniform(0,100))
    
print("Tap hop A la:",a)
print("Phan tu nho nhat la:",min(a))
print("Phan tu lon nhat la:",max(a))
print("Tong cac phan tu la:",sum(a))