bat_dau = int(input("Nhập giờ bắt đầu thuê sân (từ 5 đến 22): "))
ket_thuc = int(input("Nhập giờ kết thúc thuê sân (từ 5 đến 22): "))

if bat_dau < 5 or bat_dau > 22 or ket_thuc < 5 or ket_thuc > 22 or bat_dau >= ket_thuc:
    print("Giờ không hợp lệ.")
else:
    tien = 0

    if bat_dau < 8 and ket_thuc <= 8:
        tien = 100000 * (bat_dau - ket_thuc)
    elif bat_dau < 8 and ket_thuc > 8:
        tien = 100000 * (8 - bat_dau) + 75000 * (ket_thuc - 8)
    else:
        tien= 75000 * (ket_thuc - bat_dau)

    if 11 <= bat_dau <= 15:
        tien *= 0.9  

    print("Số tiền khách hàng phải trả là:", tien, "đồng.")