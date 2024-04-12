a = [2,-4,1,9,-3,6,3,-2,6,8]

tong_cac_ptu_trong_ds = sum(a)
print("Tong cac phan tu trong danh sach la:",tong_cac_ptu_trong_ds)

dem = 0
S = 0
for i in a:
    if i > 0:
        dem += 1
        S += i
print("Tong cac phan tu cua cac so hang duong la:",S)
print("So luong cac phan tu lon hon 0 la:",dem)

vtri_am_dau_tien = None
for j in range(len(a)):
    if a[j] < 0:
        vtri_am_dau_tien = j
        break
print("So am o vi tri dau tien la:",vtri_am_dau_tien)

vtri_duong_cuoi_cung = None
for k in range(len(a) -1,-1,-1):
    if a[k] > 0:
        vtri_duong_cuoi_cung = k
        break
print("So duong o vi tri cuoi cung la:",vtri_duong_cuoi_cung)

ptu_lon_nhat = max(a)
print("Phan tu lon nhat cua danh sach la:",ptu_lon_nhat)
vtri_lon_nhat_cuoi_cung = len(a) -1 -a[::-1].index(ptu_lon_nhat)
print("Phan tu lon nhat cua danh sach la:",ptu_lon_nhat)
print("Vi tri cua phan tu lon nhat cuoi cung la:",vtri_lon_nhat_cuoi_cung)
