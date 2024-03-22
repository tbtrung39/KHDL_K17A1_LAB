KW = float(input("Nhap so KW dien tieu thu: "))
if  KW < 100:
    gia = 2000
elif KW >= 101 and KW < 200:
    gia = 2500
elif KW >= 201 and KW < 300:
    gia = 3000
else:
    gia = 5000
tien_dien = KW * gia
print("so tien dien can thanh toan la: ", tien_dien)