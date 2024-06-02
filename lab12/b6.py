try:
    username = input("Enter Username: ")
    # Danh sách các ký tự hợp lệ (chữ cái và chữ số)
    valid_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

    for i in username:
        if i not in valid_chars:
            raise ValueError("Lỗi do chứa kí tự đặc biệt.")
except ValueError as er:
    print(er)
else:
    print("Định dạng email chính xác:")
    print(username + "@companyname.com")