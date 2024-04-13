#1a
a=[2,-4,1,9,-3,6,3,-2,6,8]
sum=0
for i in a:
    sum+=i
print("tong cac phan tu cua a la:",sum)
#1b
cac_so_hang_duong=[x for x in a if x>0]
dem_cac_so_hang_duong=len(cac_so_hang_duong)
tong_cac_so_hang_duong=sum(cac_so_hang_duong)
print("cac so hang duong la:",dem_cac_so_hang_duong)
print("tong cac so hang duong la:",tong_cac_so_hang_duong)
#1c
vi_tri_am=[vi_tri for vi_tri,gia_tri in enumerate(a) if gia_tri<0]
print("vi tri am dau tien trong danh sach la:",vi_tri_am)
#1d
vi_tri_duong=[vi_tri for vi_tri,gia_tri in enumerate(a) if gia_tri>0]
print("so hang duong dau tien trong danh sch la:",vi_tri_duong)
#1e
phan_tu_lon_nhat=max(a)
vi_tri=len(a)-a[::-1].index(phan_tu_lon_nhat)-1
print("phan tu lon nhat la:",phan_tu_lon_nhat)
print("vi tri phan tu lon nhat la:",vi_tri)