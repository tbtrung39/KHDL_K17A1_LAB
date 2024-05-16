# Tạo một từ điển rỗng lưu thông tin nhân viên
nhan_vien = {}

# Nhập số lượng nhân viên từ bàn phím
n = int(input("Nhập số lượng nhân viên: "))

# Tạo mới từ điển với thông tin của n nhân viên
for i in range(n):
    ma_nv = input("Nhập mã nhân viên (4 chữ số): ")
    ho_ten = input("Nhập họ tên nhân viên (tối đa 20 ký tự): ")
    nam_sinh = input("Nhập năm sinh: ")
    luong = float(input("Nhập lương: "))
    nhan_vien[ma_nv] = {"ho_ten": ho_ten, "nam_sinh": nam_sinh, "luong": luong}

# Thêm nhân viên mới vào từ điển
ma_nv_moi = input("Nhập mã nhân viên mới (4 chữ số): ")
ho_ten_moi = input("Nhập họ tên nhân viên mới (tối đa 20 ký tự): ")
nam_sinh_moi = input("Nhập năm sinh: ")
luong_moi = float(input("Nhập lương: "))
nhan_vien[ma_nv_moi] = {"ho_ten": ho_ten_moi, "nam_sinh": nam_sinh_moi, "luong": luong_moi}

# Tìm kiếm nhân viên theo mã nhân viên
ma_nv_tim_kiem = input("Nhập mã nhân viên cần tìm: ")
if ma_nv_tim_kiem in nhan_vien:
    print(f"Thông tin nhân viên mã {ma_nv_tim_kiem}: {nhan_vien[ma_nv_tim_kiem]}")
else:
    print("Không tìm thấy nhân viên có mã như vậy.")

# Tăng lương cho nhân viên có mã là y
ma_nv_tang_luong = input("Nhập mã nhân viên cần tăng lương: ")
if ma_nv_tang_luong in nhan_vien:
    nhan_vien[ma_nv_tang_luong]["luong"] += 1000000
    print(f"Đã tăng lương cho nhân viên mã {ma_nv_tang_luong}")

# Sắp xếp từ điển giảm dần theo năm sinh
nhan_vien_sap_xep = dict(sorted(nhan_vien.items(), key=lambda x: x[1]["nam_sinh"], reverse=True))

# In ra từ điển đã sắp xếp
print("Từ điển nhân viên sau khi sắp xếp giảm dần theo năm sinh:")
for ma_nv, thong_tin in nhan_vien_sap_xep.items():
    print(f"Mã nhân viên: {ma_nv}, Thông tin: {thong_tin}")