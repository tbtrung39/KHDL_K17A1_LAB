#diem so luong cac so hang duong va tong cua cac so hang duong
so_hang_duong=0
a=[2,-4,1,9,-3,6,3,0,-2,6,8]
tong_duong=0
for i in a:
    if i>0:
        so_hang_duong+=1
        tong_duong+=i
print("so luong cac so hang duong",so_hang_duong)
print("tong cac so hang duong",tong_duong)
#tim vi tri cau phan tu am dau tien cua danh sach
i=0
while i <len(a):
    if a[i]<0:
        vi_tri_am=i
        break
    i+=1
print("vi tri phan tu am dau tien la ",vi_tri_am)
#tim phan tu duong cuoi cung trong danh sach
for i in range(len(a)-1,-1,-1):
    if a[i]>0:
        vi_tri_duong=i
        break
#tim vi tri lon nhat trong danh sachva vi tri lon nhat cuoi cung
a.reverse
print(a)
max=0
vi_tri=0
for i in range(0,len(a)):
    if a[i]>max:
        max=a[i]
        vi_tri=i
print(f"phan tu lon nhat trong danh sach la:{max},va vi tri cua phan tu lon nhat la:{vi_tri}")
    

