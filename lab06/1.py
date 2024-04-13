a=[2,-4,1,9,-3,6,3,-2,6,8]
print("Tổng của list la:",sum(a))
dem=0
tong=0
for so in a:
    if so>0:
        dem+=1
        tong+=so
print("so luong cac so hạng dương trong list",dem)
print("Tông của các số hạng dương trong list:",tong)
vi_tri_dau_tien=a.index(next((so for so in a if so<0),None))
print("Vị tri phần tử dầu tiên trong list:",vi_tri_dau_tien)
vi_tri_duong_cuoi_cung=len(a)-1-a[::1].index(next((so for so in a[::1] if so>0),None))
print("Vi tri phan tu duong cuói cùng trong list:",vi_tri_duong_cuoi_cung)
phân_tu_lon_nhat=max(a)
print("Phân tử lớn nhất:",phân_tu_lon_nhat)
vi_tri_lon_nhat_cuoi_cung=len(a)-1-a[::1].index(max(a))
print("Vị trí lớn nhất cuối cùng trong ds:",vi_tri_lon_nhat_cuoi_cung)