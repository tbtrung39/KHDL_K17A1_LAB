so_nguyen = int(input("Nhập vào một số nguyên: "))
if so_nguyen < 100:
    print("Không có chữ số hàng trăm.")
elif so_nguyen < 1000:
    print("Chữ số hàng trăm của số đó là:", so_nguyen // 100)
elif so_nguyen >1000:
    print("0")