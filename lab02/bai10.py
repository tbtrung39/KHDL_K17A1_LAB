import math 
n = int(input("Nhập vào giờ bắt đầu(5-22): "))
z = int(input("Nhập giờ kết thúc(5-22): "))
if 5 <= n <= z <= 22:
    tong_so_gio = z-n
    if 0 < tong_so_gio <= 3:
        print("Số tiền khách thuê sân tập phải trả là: ", tong_so_gio*100000, "VND")
    else:
        so_tien = 3*100000 + (tong_so_gio-3)*(100000*0.75)
        print("Số tiền khách thuê sân tập phải trả là: ", so_tien, "VND")