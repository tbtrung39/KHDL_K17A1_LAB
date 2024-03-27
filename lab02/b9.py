n = int(input("Nhập số kW tiêu thụ: "))
if n > 0:
    if n > 0 and n <= 100:
        don_gia = 2000
        tien_dien = don_gia * n
        print("Tiền điện: ", tien_dien)
    elif n > 100 and n <= 200:
        don_gia = 2500
        tien_dien = don_gia * n
        print("Tiền điện: ", tien_dien)
    elif n > 100 and n <= 200:
        don_gia = 3000
        tien_dien = don_gia * n
        print("Tiền điện: ", tien_dien)
    else:
        don_gia = 5000
        tien_dien = don_gia * n
        print("Tiền điện: ", tien_dien)
else:
    print("Vui lòng nhập lại")