import re

mat_khau_nhap_vao = input("Nhập mật khẩu (các mật khẩu phân tách nhau bởi dấu phẩy): ").split(',')

mat_khau_hop_le = []
for mat_khau in mat_khau_nhap_vao:
    mat_khau = mat_khau.strip()
    if len(mat_khau) >= 6 and len(mat_khau) <= 12 and re.search("[a-z]", mat_khau) and re.search("[0-9]", mat_khau) and re.search("[A-Z]", mat_khau) and re.search("[$#@]", mat_khau):
        mat_khau_hop_le.append(mat_khau)

print("Các mật khẩu hợp lệ là:")
for mat_khau in mat_khau_hop_le:
    print(mat_khau, end=", ")
