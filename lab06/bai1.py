a = [2,-4,1,9,-3,6,3,-2,6,8]
tong_a = sum(a)
print("Tổng các phần tử trong danh sách =", tong_a) 
so_phan_tu_duong = [x for x in a if x > 0]
so_luong_phan_tu_duong = len(so_phan_tu_duong)
tong_cac_phan_tu_duong = sum(so_phan_tu_duong)
print("Số lượng các số hạng dương: ",so_luong_phan_tu_duong)
print("Tổng các số hạng dương là: ",tong_cac_phan_tu_duong)
vi_tri_pt_am_dau_tien = None
for i in range(len(a)):
    if a[i] < 0:
        vi_tri_pt_am_dau_tien = i
        break
print("Vị trí phần tử âm đầu tiên trong danh sách: ",vi_tri_pt_am_dau_tien)
vi_tri_pt_duong_cuoi_cung = None
for j in range(len(a)-1,-1,-1):
    if a[j] > 0:
        vi_tri_pt_duong_cuoi_cung = j
        break
print("Vị trí phần tử dương cuối cùng trong danh sách: ",vi_tri_pt_duong_cuoi_cung)
sap_xep_a = sorted(a)
print(sap_xep_a)
phan_tu_lon_nhat = sap_xep_a[-1]
vi_tri_phan_tu_lon_nhat = a.index(phan_tu_lon_nhat)
print("Phần tử lớn nhất danh sach ", phan_tu_lon_nhat)
print("Vị trí phần tử lớn nhất danh sách: ", vi_tri_phan_tu_lon_nhat)