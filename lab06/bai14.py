pas = input("Nhập mật khẩu, cách nhau bởi dấu phẩy: ").split(', ')
valid = []
l, u, p, d = 0, 0, 0, 0  
for password in pas:
    for i in password:
        if i.islower():
            l += 1
        if i.isupper():
            u += 1
        if i.isdigit():
            p += 1
        if i in ('@', '$', '#'):
            d += 1
    if l >= 1 and u >= 1 and p >= 1 and d >= 1 and len(password) >= 6 and len(password) <= 12:
        valid.append(password)
if valid:
    print("Mật khẩu hợp lệ:", ", ".join(valid))
else:
    print("Không có mật khẩu hợp lệ")
