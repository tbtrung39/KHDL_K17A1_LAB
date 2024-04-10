# Nhập số phần tử từ người dùng
n = int(input("Nhập số phần tử của danh sách: "))

# Khởi tạo danh sách và nhập các phần tử từ người dùng
danh_sach = []
for i in range(n):
    phan_tu = int(input("Nhập phần tử thứ {}: ".format(i + 1)))
    danh_sach.append(phan_tu)
# Tìm phần tử lớn thứ 2 và vị trí của nó
danh_sach.sort(reverse=True)
phantu_lon_thu_hai = danh_sach[1]
vi_tri_phantu_lon_thu_hai = danh_sach.index(phantu_lon_thu_hai) + 1
# Tính số lượng các số dương liên tiếp nhiều nhất
max_so_luong_duong = 0
current_so_luong_duong = 0
for phan_tu in danh_sach:
    if phan_tu > 0:
        current_so_luong_duong += 1
        max_so_luong_duong = max(max_so_luong_duong, current_so_luong_duong)
    else:
        current_so_luong_duong = 0

# Tính số lượng các số dương liên tiếp có tổng lớn nhất
max_tong_duong = 0
current_tong_duong = 0
for phan_tu in danh_sach:
    if phan_tu > 0:
        current_tong_duong += phan_tu
        max_tong_duong = max(max_tong_duong, current_tong_duong)
    else:
        current_tong_duong = 0
# In kết quả
print("Phần tử lớn thứ 2 là:", phantu_lon_thu_hai)
print("Vị trí của phần tử lớn thứ 2 trong danh sách là:", vi_tri_phantu_lon_thu_hai)
print("Số lượng các số dương liên tiếp nhiều nhất là:", max_so_luong_duong)
print("Số lượng các số dương liên tiếp có tổng lớn nhất là:", max_tong_duong)
