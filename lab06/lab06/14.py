import re
cac_mat_khau = input("Nhập các mật khẩu, phân tách bởi dấu phẩy: ").split(',')
mat_khau_hop_le = []
for mat_khau in cac_mat_khau:
    if not re.search("[a-z]", mat_khau):
        continue
    if not re.search("[0-9]", mat_khau):
        continue
    if not re.search("[A-Z]", mat_khau):
        continue
    if not re.search("[$#@]", mat_khau):
        continue
    if len(mat_khau) < 6 or len(mat_khau) > 12:
        continue
    mat_khau_hop_le.append(mat_khau)
print("Các mật khẩu hợp lệ là:",mat_khau_hop_le)

