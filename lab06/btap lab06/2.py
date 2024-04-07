n = int(input("Nhập số phần tử của danh sách: "))
danh_sach = []
for i in range(n):
    phan_tu = int(input(f"Nhập phần tử thứ {i + 1}: "))
    danh_sach.append(phan_tu)
danh_sach_a = danh_sach.copy()
max1 = max(danh_sach_a)
danh_sach_a.remove(max1)
max2 = max(danh_sach_a)
vi_tri_max2 = danh_sach_a.index(max2)
print("Danh sách:", danh_sach)
print("Phần tử lớn thứ hai trong danh sách là:", max2)
print("Vị trí của phần tử lớn thứ hai trong danh sách là:", vi_tri_max2)
#########################################################################
max_so_luong = 0
so_luong_hien_tai = 0
for so in danh_sach:
    if so > 0:
        so_luong_hien_tai += 1
        max_so_luong = max(max_so_luong, so_luong_hien_tai)
    else:
        so_luong_hien_tai = 0
print("Số lượng các số dương liên tiếp nhiều nhất là:", max_so_luong)
#########################################################################
max_so_luong = 0
so_luong_hien_tai = 0
max_tong = 0
tong_hien_tai = 0
for so in danh_sach:
    if so > 0:
        so_luong_hien_tai += 1
        tong_hien_tai += so
        max_tong = max(max_tong, tong_hien_tai)
    else:
        so_luong_hien_tai = 0
        tong_hien_tai = 0

    if tong_hien_tai == max_tong:
        max_so_luong = max(max_so_luong, so_luong_hien_tai)
print("Số lượng các số dương liên tiếp có tổng lớn nhất là:", max_so_luong)
