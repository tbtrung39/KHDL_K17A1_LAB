while True:
    mat_khau = input("Nhập mật khẩu mới: ")
    hop_le = True

    if len(mat_khau) < 6 or len(mat_khau) > 12:
        print("Độ dài mật khẩu phải từ 6 đến 12 ký tự.")
        hop_le = False

    if not any(c.islower() for c in mat_khau):
        print("Mật khẩu phải chứa ít nhất 1 ký tự thường (a-z).")
        hop_le = False

    if not any(c.isupper() for c in mat_khau):
        print("Mật khẩu phải chứa ít nhất 1 ký tự hoa (A-Z).")
        hop_le = False

    if not any(c.isdigit() for c in mat_khau):
        print("Mật khẩu phải chứa ít nhất 1 chữ số (0-9).")
        hop_le = False

    if not any(c in "$#@ " for c in mat_khau):
        print("Mật khẩu phải chứa ít nhất 1 ký tự đặc biệt trong ($#@).")
        hop_le = False

    if hop_le:
        print("Mật khẩu hợp lệ!")
        break