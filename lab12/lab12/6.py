try:
    username = input("Nhập Tên người dùng: ")
    # Danh sách các ký tự hợp lệ (chữ và chữ số)
    valid_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

    for char in username:
        if char not in valid_chars:
            raise ValueError("Lỗi do chứa ký tự đặc biệt.")

    print("Chính xác định dạng email:", username + "@companyname.com")
except ValueError as err:
    print(err)
