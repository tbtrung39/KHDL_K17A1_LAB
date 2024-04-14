chuoi_mat_khau = input("Nhập chuỗi mật khẩu, phân tách bởi dấu phẩy: ")
mat_khau_list = chuoi_mat_khau.split(', ')
mat_khau_hop_le = []
for mat_khau in mat_khau_list:
    co_chu_cai_thuong = False
    co_so = False
    co_chu_cai_in_hoa = False
    co_ky_tu_dac_biet = False
    for char in mat_khau:
        if char.islower():
            co_chu_cai_thuong = True
        elif char.isdigit():
            co_so = True
        elif char.isupper():
            co_chu_cai_in_hoa = True
        elif char in ['$','#','@',')']:
            co_ky_tu_dac_biet = True
    if 6 <= len(mat_khau) <= 12 and co_chu_cai_thuong and co_so and co_chu_cai_in_hoa and co_ky_tu_dac_biet:
        mat_khau_hop_le.append(mat_khau)

print(', '.join(mat_khau_hop_le))
