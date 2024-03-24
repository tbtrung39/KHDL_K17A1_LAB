so_nguyen = int(input("Nhập vào một số nguyên: "))

if 100 <= so_nguyen <= 999:
    hang_tram = so_nguyen // 100
    print("Chữ số hàng trăm của số", so_nguyen, "là:", hang_tram)
else:
    print("Số không có chữ số hàng trăm. Xuất ra 0.")