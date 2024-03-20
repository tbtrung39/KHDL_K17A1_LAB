#1
n = int(input("Nhập vào tháng: "))
if n <= 12 and n >=1:
    if n == 4 or n == 6 or n == 9 or n == 11:
        print("30 ngày ")
    elif n == 2:
        print(" 28 hoặc 29 ngày")
    else:
        print("31 ngày")
else:
    print("không tồn tại tháng")
#2
import math

a = float(input("Nhập a:"))
b = float(input("Nhập b:"))
c = float(input("Nhập c:"))
delta = b**2 - 4*a*c 
if a == 0:
    x = -c/b
    print("Phương trình có no duy nhất: ", x)
else:
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / 2*a
        x2 = (-b - math.sqrt(delta)) / 2*a
        print("Phương trình có 2 no phân biệt: ",x1,",",x2)
    elif delta == 0: 
        x0 = -b / 2*a
        print("Phương trình có 2 no kép: ", x0)
    else:
        print("Phương trình vô no")
#3
n = int(input("Nhập vào ngày trong tuần: "))
if n <= 7 and n >= 1:
    if n == 1:
        print("Sunday")
    elif n == 2:
        print("Monday")
    elif n == 3:
        print("Tuesday")
    elif n == 4:
        print("Wednesday")
    elif n == 5:
        print("Thursday")
    elif n == 6:
        print("Friday")
    elif n == 7:
        print("Saturday")
else: 
    print("Không tồn tại ngày này ")
#4
n = int(input("Nhập vào số cần xét: "))
a = n /100
if a % 100 >= 1:
    print(f"chữ số hàng trăm của số đó là {a:.0f}")
else:
    print("0")
#5
n = int(input("Nhập vào tháng trong năm: "))
if n <= 12 and n >= 1:
    if n == 1:
        print("January")
    elif n == 2:
        print("February")
    elif n == 3:
        print("March")
    elif n == 4:
        print("April")
    elif n == 5:
        print("May")
    elif n == 6:
        print("June")
    elif n == 7:
        print("July")
    elif n == 8:
        print("August")
    elif n == 9:
        print("September")
    elif n == 10:
        print("October")
    elif n == 11:
        print("November")
    else:
        print("December")
else: 
    print("Không tồn tại tháng này ")
#6
num = int(input("Nhập số nguyên có ba chữ số: "))
a = num // 100
b = (num % 100) // 10
c = num % 10
if a == 1:
    print("Một trăm", end=' ')
elif a == 2:
    print("Hai trăm", end=' ')
elif a == 3:
    print("Ba trăm", end=' ')
elif a == 4:
    print("Bốn trăm", end=' ')
elif a == 5:
    print("Năm trăm", end=' ')
elif a == 6:
    print("Sáu trăm", end=' ')
elif a == 7:
    print("Bảy trăm", end=' ')
elif a == 8:
    print("Tám trăm", end=' ')
elif a == 9:
    print("Chín trăm", end=' ')
if b != 0:
    if b == 1:
        print("mười", end=' ')
    elif b == 2:
        print("hai mươi", end=' ')
    elif b == 3:
        print("ba mươi", end=' ')
    elif b == 4:
        print("bốn mươi", end=' ')
    elif b == 5:
        print("năm mươi", end=' ')
    elif b == 6:
        print("sáu mươi", end=' ')
    elif b == 7:
        print("bảy mươi", end=' ')
    elif b == 8:
        print("tám mươi", end=' ')
    elif b == 9:
        print("chín mươi", end=' ')
if c != 0 and b != 1:
    if c == 1:
        print("một")
    elif c == 2:
        print("hai")
    elif c == 3:
        print("ba")
    elif c == 4:
        print("bốn")
    elif c == 5:
        print("lăm")
    elif c == 6:
        print("sáu")
    elif c == 7:
        print("bảy")
    elif c == 8:
        print("tám")
    elif c == 9:
        print("chín")
#7
n = int(input("Nhập điểm hệ : "))
if n > 10 and n < 0:
    print("Vui lòng nhập lại")
else:
    if n >= 0 and n < 3:
        print("Kém")
    elif n >= 3 and n < 5:
        print("Yếu")
    elif n >= 5  and n <7:
        print("Trung bình")
    elif n >= 7 and n < 9:
        print("Khá")
    else:
        print("Giỏi")
#8
n = int(input("Nhập số tháng làm việc: "))
if n < 12:
    luong1 = 2.34 * 1350000
    print("Lương bằng: ", luong1)
if n >= 12 and n < 36:
    luong2 = 3.33 * 1350000
    print("Lương bằng: ", luong2)
if n >= 36 and n < 60:
    luong3 = 3.66 * 1350000
    print("Lương bằng: ", luong3)
if n >= 60:
    luong4 = 3.99 * 1350000
    print("Lương là: ", luong4)
#9
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
#10
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
    elif gio_thue > 15:
        so_tien4 = 300000 + (75000 * (gio_thue-3))
        print("số tiền phải trả là ",so_tien4)
else: 
    print("Sân chưa mở cửa")
#11
m = int(input("nhập vào ngày cho trước: "))
n = int(input("Nhập vào tháng: "))
if n <= 12 and n >=1:
    if n == 4 or n == 6 or n == 9 or n == 11:
        if m >= 1 and m <= 30:
            l = m + 1
            if l == 31:
                print("ngày mùng 1")
            else:
                print(f"ngày sau ngày cho trước là ngày {l}")
        else:
            print("không tồn tại ngày")
    elif n == 2:
        if m >= 1 and m <= 28:
            l = m + 1
            if l == 29:
                print("ngày mùng 1")
            else:
                print(f"ngày sau ngày cho trước là ngày {l}")
        else:
            print("không tồn tại ngày")
    else:
        if m >= 1 and m <= 31:
            l = m + 1
            if l == 32:
                print("ngày mùng 1")
            else:
                print(f"ngày sau ngày cho trước là ngày {l}")
        else:
            print("không tồn tại ngày này")
else:
    print("không tồn tại tháng")
