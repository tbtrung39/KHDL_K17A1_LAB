c = int(input("Nhập vào số nguyên là:"))
chu_so_hang_tram = (c // 100) % 10
if chu_so_hang_tram != 0:
    print(c,"chữ so hàng trăm là:",chu_so_hang_tram)
else:
    print(c,"không có chữ số hàng trăm")