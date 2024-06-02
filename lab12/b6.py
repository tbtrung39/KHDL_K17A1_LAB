def kiem_tra_username(username):
    if not username.isalnum():
        raise ValueError("Username chỉ được chứa chữ cái và số.")
    return True

try:
    danh_sach_email = []

    while True:
        username = input("Nhập username của nhân viên (không chứa dấu cách): ")
        if kiem_tra_username(username):
            email = username + '@companyname.com'
            danh_sach_email.append(email)
            print("Email của nhân viên là:", email)

except ValueError as ve:
    print("Lỗi:", ve)
except KeyboardInterrupt:
    print("\nQuá trình nhập đã bị ngắt bởi người dùng.")
