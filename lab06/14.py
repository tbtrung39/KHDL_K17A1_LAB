mat_khau = input("Nhập mật khẩu (các mật khẩu phân tách nhau bởi dấu phẩy): ")
danh_sach_mat_khau = mat_khau.split(',')
for mk in danh_sach_mat_khau:
    mk = mk.strip() 
    if len(mk) < 6 or len(mk) > 12:
        continue
    if not any(char.islower() for char in mk):
        continue
    if not any(char.isupper() for char in mk):
        continue
    if not any(char.isdigit() for char in mk):
        continue
    if not any(char in ['$','#','@'] for char in mk):
        continue
    print(mk)
