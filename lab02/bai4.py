# Nhập số nguyên từ người dùng
so_nguyen = int(input("Nhập số nguyên: "))

# Xác định chữ số hàng trăm và in ra
if so_nguyen >= 100:
    hang_tram = (so_nguyen // 100) % 10
    print("Chữ số hàng trăm của số đó là:", hang_tram)
else:
    print("0")
