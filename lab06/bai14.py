mat_khau = input("Nhập các mật khẩu, phân tách bởi dấu phẩy: ")
ma = mat_khau.split(',')
in_mat_khau = []
a = "abcdefghijklmnopqrstuvwxyz"
b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c = "0123456789"
d = "$#@"
for password in ma:
    if 6 <= len(password) <= 12:
        has_a = any(char in a for char in password)
        has_b = any(char in b for char in password)
        has_number = any(char in c for char in password)
        has_special_char = any(char in d for char in password)

        if has_a and has_b and has_number and has_special_char:
            in_mat_khau.append(password)
print(",".join(in_mat_khau))