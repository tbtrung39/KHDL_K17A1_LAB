a = int(input("Giờ bắt đầu: "))
b = int(input("Giờ kết thúc: "))
gio_thue = int(b - a)
if gio_thue >= 5 and gio_thue <= 22:
    if gio_thue > 0 and gio_thue <= 3:
        tien_thue1 = 100000
        so_tien1 = tien_thue1 * gio_thue
        print("Số tiền phải trả: ", so_tien1)
    elif gio_thue > 3 and gio_thue < 11:
        tien_thue2 = 75000
        so_tien2 = 300000 + (tien_thue2 * (gio_thue-3)) 
        print("Số tiền phải trả: ", tien_thue2)
    elif gio_thue >= 11 and gio_thue <= 15:
        so_tien3 = (300000 + ((gio_thue-3) * 75000)) * 90/100
        print("Số tiền cần phải trả: ", so_tien3)
    else:
        print("Quá số giờ thuê sân")
else: 
    print("Sân chưa mở cửa")