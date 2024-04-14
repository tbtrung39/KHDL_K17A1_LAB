a = [2,-4,1,9,-3,6,3,-2,6,8]
print("tong la", sum(a))

so_luong_duong=0
tong_so_duong=0
for i in a :
    if i >0:
        so_luong_duong+=1
        tong_so_duong+=i
print("so luong so duong trong a la",so_luong_duong)
print('tong so duong trong a la',tong_so_duong)
# tim vi tri của phan tử am trong danh sach 
vi_tri_am_dau_tien=a.index(-4)
print(" vi tri am dau tien la ",vi_tri_am_dau_tien)
vi_tri_duong_cuoi_cung=a.index(8)
print(" vi tri duong cuoi cung la ", vi_tri_duong_cuoi_cung)
# tim phan tu lon nhat cua danh sach va tim vi tri 
print(" phan tu lon nhat của danh sach la ",max(a))
vi_tri_ptu_lon_nhat=a.index(max(a))
print("vi tri phan tu lon nhat la ",vi_tri_ptu_lon_nhat)