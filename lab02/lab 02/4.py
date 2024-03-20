#Nhập vào 1 số nguyên, yêu cầu xuất ra chữ số hàng trăm của số đó, nếu không có thì xuất ra 0.
numbers=int(input("moi nhap so:"))
if (numbers>100) or (numbers<=999):
    chu_so_hang_tram=numbers/100
    print("chu so hang tram cua so thoa man la:",chu_so_hang_tram)
else:
    print("xuat ra so 0:")