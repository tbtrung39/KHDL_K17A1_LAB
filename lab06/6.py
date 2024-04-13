#6
import random
a=[]
for i in range(1000):
    so_ngau_nhien=random.randit(1,99999)
    a.append(so_ngau_nhien)
print(a)
# dung ham sorted
danh_sach_1=sorted(a)
print("chuoi khi duoc sap xep la:",danh_sach_1)