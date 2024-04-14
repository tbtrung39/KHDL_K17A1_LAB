#Yeu cau 1:Sinh mot list gom 1000 so trong [1,99999]
import random

danh_sach=[]

for _ in range (1000):
    so_ngau_nhien=random.randint(1,100000)
    danh_sach.append(so_ngau_nhien)
    
print("Day so ngau nhien: ",danh_sach)
#Yeu cau 2: Sap xep tang dan, giam dan bang sorted
danh_sach1 =sorted(danh_sach,key=lambda x:x)
print("Danh sach lon dan la:",danh_sach1)
danh_sach2 =sorted(danh_sach,key=lambda x:x,reverse=True)
print("Danh sach be dan la:",danh_sach2)
