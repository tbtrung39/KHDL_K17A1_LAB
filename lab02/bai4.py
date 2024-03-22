so_nguyen = int(input("Nhập vào một số nguyên: "))
if so_nguyen >= 100 and so_nguyen <= 999:
    hang_tram = so_nguyen // 100
    print("Chữ số hàng trăm của số bạn nhập là:", hang_tram)
else:
    print("0")
