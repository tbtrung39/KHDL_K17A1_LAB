gia_tien_san_1h=100000
gio_bat_dau = float(input("Nhap vao gio bat dau:"))
gio_ket_thuc = float(input("Nhap vao gio ket thuc:"))
time=gio_ket_thuc-gio_bat_dau
if 5.0<=time<=22.0:
    if time<=3:
        tien_san = gia_tien_san_1h*time
        print(tien_san)
    elif time>3:
        tien_san=gia_tien_san_1h*time*0.75
        print(tien_san)
    elif 11<=time<=15:
        tien_san=gia_tien_san_1h*time*0.9
        print(tien_san)
    else:
        print("error,please try again")
else:
    print('try again')