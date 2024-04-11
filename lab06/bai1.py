a=[2,-4,1,9,-3,6,-2,6,8]
tong=0
for i in a:
    tong+=i
print("tong cac phan tu la:", tong)

dem=0
tong_duong=0
for i in a:
    if i >0:
        dem+=1
        tong_duong+=1
print("so phan tu duong la:", dem)
print("tong duong la:", tong_duong)

for i in a:
    if i<0:
        break
print("so phan tu am dau tien la:", i)

a.reverse()
for i in a: 
    if i>0:
        break
print("so duong cuoi cung la:", i)

a.reverse()
index=1
vi_tri_lon_nhat=0
max=0
for i in a:
    if max<i:
        max=i
        vi_tri_lon_nhat=index
    index+=1
print("vi tri phan tu lon nhat:", vi_tri_lon_nhat)
print("so lon nhat la:", max)