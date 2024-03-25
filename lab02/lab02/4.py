so = int(input("Nhập vào một số nguyên: "))

if so >= 100 and so <= 999:
    so_hang_tram = so // 100 
    print("Chữ số hàng trăm là:", so_hang_tram)
else:
    print("0")