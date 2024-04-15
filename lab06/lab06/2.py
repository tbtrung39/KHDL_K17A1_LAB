n = int(input("nhập số phần tử của danh sách: "))
danh_sach = []

for i in range(n):
    so = int(input(f"nhập phần tử thứ {i+1}: "))
    danh_sach.append(so)

danh_sach.sort(reverse=True)
lon_thu_hai = danh_sach[1]
vi_tri = danh_sach.index(lon_thu_hai) + 1
print(f"phần tử lớn thứ hai của danh sách là {lon_thu_hai} và nằm ở vị trí {vi_tri}")
so_luong_max = 0
so_luong_hien_tai = 0
for so in danh_sach:
    if so > 0:
        so_luong_hien_tai += 1
        so_luong_max = max(so_luong_max, so_luong_hien_tai)
    else:
        so_luong_hien_tai = 0
print(f"số lượng các số dương liên tiếp nhiều nhất là {so_luong_max}")
tong_max = 0
tong_hien_tai = 0
for so in danh_sach:
    if so > 0:
        tong_hien_tai += so
        tong_max = max(tong_max, tong_hien_tai)
    else:
        tong_hien_tai = 0
print(f"tổng của dãy số dương liên tiếp lớn nhất là {tong_max}")