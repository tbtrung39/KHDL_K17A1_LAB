# Nhập chuỗi mật khẩu từ người dùng, phân tách bởi dấu phẩy
chuoi_mat_khau = input("Nhập chuỗi mật khẩu, phân tách bởi dấu phẩy: ")

# Tách các mật khẩu trong chuỗi
mat_khau_list = chuoi_mat_khau.split(', ')

# Khởi tạo một danh sách để lưu trữ các mật khẩu hợp lệ
mat_khau_hop_le = []

# Kiểm tra tính hợp lệ của từng mật khẩu và thêm vào danh sách nếu hợp lệ
for mat_khau in mat_khau_list:
    # Khởi tạo các biến kiểm tra
    co_chu_cai_thuong = False
    co_so = False
    co_chu_cai_in_hoa = False
    co_ky_tu_dac_biet = False
    
    # Kiểm tra từng ký tự trong mật khẩu
    for char in mat_khau:
        # Yêu cầu a: Ít nhất 1 chữ cái nằm trong [a-z]
        if char.islower():
            co_chu_cai_thuong = True
        # Yêu cầu b: Ít nhất 1 số nằm trong [0-9]
        elif char.isdigit():
            co_so = True
        # Yêu cầu c: Ít nhất 1 kí tự nằm trong [A-Z]
        elif char.isupper():
            co_chu_cai_in_hoa = True
        # Yêu cầu d: Ít nhất 1 ký tự nằm trong [$ # @,)
        elif char in ['$','#','@',')']:
            co_ky_tu_dac_biet = True
    
    # Yêu cầu e: Độ dài mật khẩu tối thiểu: 6 ký tự
    # Yêu cầu f: Độ dài mật khẩu tối đa: 12 ký tự
    if 6 <= len(mat_khau) <= 12 and co_chu_cai_thuong and co_so and co_chu_cai_in_hoa and co_ky_tu_dac_biet:
        mat_khau_hop_le.append(mat_khau)

# In ra các mật khẩu hợp lệ, cách nhau bởi dấu phẩy
print(', '.join(mat_khau_hop_le))
