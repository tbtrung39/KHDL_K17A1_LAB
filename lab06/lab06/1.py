a=[2, -4, 1, 9, -3, 6, 3,-2, 6, 8]
#tinh tong cac phan tu cua danh sach
tong=sum(a)
print("tong cac phan tu cua danh sach la:", tong)
#dem so luong so hang duong va tinh tong cua cac so hang duong
dem_so_luong=sum(1 for x in a if x>0)
tong_so_duong=sum(x for x in a if x>0)
print("so luong so hang duong la:", dem_so_luong)
print("tong cua cac so hang duong la:", tong_so_duong)
#tim vi tri cua phan tu am dau tien
vi_tri_am_dau_tien= next((i for i, x in enumerate(a) if x<0), None)
print("vi tri cua phan tu am dau tien trong danh sach la:", vi_tri_am_dau_tien)
#tim vi tri cua phan tu duong cuoi cung
vi_tri_duong_cuoi_cung= len(a)-1-next((i for i, x in enumerate(reversed(a)) if x>0), None)
print("vi tri cua phan tu duong cuoi cung trong danh sach la:", vi_tri_duong_cuoi_cung)
#tim phan tu lon nhat cua danh sach va vi tri phan tu lon nhat cuoi cung
phan_tu_lon_nhat=max(a)
vi_tri_max_cuoi_cung= len(a)-1-next((i for i, x in enumerate(reversed(a)) if x==phan_tu_lon_nhat), None)
print("phan tu lon nhat cua danh sach la:", phan_tu_lon_nhat)
print("vi tri cua phan tu lon nhat cuoi cung trong danh sach la:", vi_tri_max_cuoi_cung)