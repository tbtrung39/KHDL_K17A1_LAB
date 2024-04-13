while True:
    mat_khau = input("Nhập mật khẩu mới: ")
    if len(mat_khau) < 6 or len(mat_khau) > 12:
        print("Độ dài mật khẩu phải từ 6-12 kí tự")
    elif not any(c.islower() for c in mat_khau):
        print("Mật khẩu phải có ít nhất 1 chữ trong (a-z)")
    elif not any(c.isupper() for c in mat_khau):
        print("Mật khẩu phải có ít nhất 1 chữ trong (A-Z)")
    elif not any(c.isdigit() for c in mat_khau):
        print("Mật khẩu phải có ít nhất 1 chữ số trong (0-9)")
    elif not any(c in "$#@ " for c in mat_khau):
        print("Mật khẩu phải có ít nhất 1 kí tự đặc biệt trong ($#@)")
    else:
        print("Đặt mật khẩu thành công")
        break