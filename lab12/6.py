try:
    ten = input("Nhap ten: ")
    # Danh sách các ký tự hợp lệ (chữ cái và chữ số)
    legit = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

    for i in ten:
        if i not in legit:
            raise ValueError("Lỗi do chứa kí tự đặc biệt.")
except ValueError as er:
    print(er)
else:
    print("Định dạng email chính xác:")
    print(ten + "@companyname.com")