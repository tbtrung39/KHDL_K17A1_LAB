gia_3_gio_dau= 100000
gia_giam_gia_cac_gioi_sau= 0.25
gia_trong_gio_uu_dai=0.1
gio_bat_dau=int(input("nhập giờ bắt đầu: "))
gio_ket_thuc=int(input("nhập giờ kết thúc: "))
if gio_bat_dau <5 or gio_bat_dau > 22 or gio_ket_thuc <5 or gio_ket_thuc >22 or gio_ket_thuc < gio_bat_dau:
    print("Giờ không hợp lệ!!!")
else:
    gia_thue=0
    so_gio_thue=gio_ket_thuc-gio_bat_dau
    if so_gio_thue<=3:
        gia_thue = so_gio_thue * gia_3_gio_dau
    else:
        gia_thue = 3* gia_3_gio_dau
        so_gio_con_lai=so_gio_thue-3
        gia_thue += so_gio_con_lai * (gia_3_gio_dau * (1- gia_giam_gia_cac_gioi_sau) **3)
    if 11<=gio_bat_dau <=15 and gio_ket_thuc >=15:
        gia_thue *= (1-gia_giam_gia_cac_gioi_sau)

    print("số tiền phải trả là:", gia_thue)