#Nhập vào 1 số nguyên, yêu cầu xuất ra chữ số hàng trăm của số đó, nếu không có thì xuất ra 0.
so_nguyen=int(input("moi nhap so nguyen"))
if (so_nguyen >100) or (so_nguyen<=999):
    chu_so_hang_tram=so_nguyen/100
    print("xuat ra chu so hang tram",chu_so_hang_tram)
else:
    print("xuat ra chu so 0")