#Yeu cau: Sinh mot list gom 1000 so trong [1,99999]
import random

danh_sach=[]

for _ in range (1000):
    so_ngau_nhien=random.randint(1,100000)
    danh_sach.append(so_ngau_nhien)
    
print("Day so ngau nhien: ",danh_sach)