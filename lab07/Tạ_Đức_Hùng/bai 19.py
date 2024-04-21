# Tạo mới từ điển
n = int(input("Nhập số lượng nhân viên: "))
nhan_vien = {}

# Thêm thông tin cho từ điển
print("Nhập thông tin cho từ điển:")
for i in range(n):
    ma_nv = input("Nhập mã nhân viên (4 chữ số): ")
    ho_ten = input("Nhập họ tên nhân viên (20 ký tự): ")
    nam_sinh = input("Nhập năm sinh nhân viên: ")
    luong = float(input("Nhập lương nhân viên: "))
    nhan_vien[ma_nv] = {'Họ và tên': ho_ten, 'Năm sinh': nam_sinh, 'Lương': luong}

# Tìm kiếm nhân viên theo mã
ma_nv_tim_kiem = input("Nhập mã nhân viên cần tìm kiếm: ")
if ma_nv_tim_kiem in nhan_vien:
    print(f"Thông tin của nhân viên có mã {ma_nv_tim_kiem}: {nhan_vien[ma_nv_tim_kiem]}")
else:
    print("Không tìm thấy nhân viên có mã này.")

# Tăng lương cho nhân viên
ma_nv_tang_luong = input("Nhập mã nhân viên cần tăng lương: ")
if ma_nv_tang_luong in nhan_vien:
    nhan_vien[ma_nv_tang_luong]['Lương'] += 1000000
    print(f"Đã tăng lương cho nhân viên có mã {ma_nv_tang_luong}.")
else:
    print("Không tìm thấy nhân viên có mã này.")

# Xóa nhân viên
ma_nv_xoa = input("Nhập mã nhân viên cần xóa: ")
if ma_nv_xoa in nhan_vien:
    del nhan_vien[ma_nv_xoa]
    print(f"Đã xóa nhân viên có mã {ma_nv_xoa}.")
else:
    print("Không tìm thấy nhân viên có mã này.")

# Sắp xếp từ điển giảm dần theo năm sinh
nhan_vien_sap_xep = sorted(nhan_vien.items(), key=lambda x: x[1]['Năm sinh'], reverse=True)
# In ra danh sách nhân viên đã sắp xếp
print("\nDanh sách nhân viên sau khi sắp xếp:")
for ma_nv, thong_tin in nhan_vien_sap_xep:
    print(f"Mã nhân viên: {ma_nv}, Họ và tên: {thong_tin['Họ và tên']}, Năm sinh: {thong_tin['Năm sinh']}, Lương: {thong_tin['Lương']}")