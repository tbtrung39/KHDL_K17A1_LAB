import random 
A=set()
n=input("nhap so lương phan tu:")
while len(A)<int(n):
  A.add(random.random())
print("tap hop A:",A)
print("phan tu lon nhat:",max(A))
print("phan tu nho nhat:",min(A))
print("tong cac phan tu cua A:",sum(A))