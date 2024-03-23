#1
thang = int(input("nhập tháng kiểm tra :"))
if thang ==1:
        print("tháng có 31 ngày")
elif thang == 2:
        print("tháng có 28 hoặc 29")    
elif thang ==3:
        print("tháng có 31 ngày")
elif thang ==4:
        print("tháng có 30 ngày")
elif thang ==5:
        print("tháng có 31 ngày")
elif thang ==6:
        print("tháng có 30 ngày")
elif thang ==7:
        print("tháng có 31 ngày")
elif thang ==8:
        print("tháng có 31 ngày")
elif thang ==9:
        print("tháng có 310ngày")
elif thang ==10:
        print("tháng có 31 ngày")
elif thang ==11:
        print("tháng có 30 ngày")
elif thang ==12:
        print("tháng có 31 ngày")
else:
        print("bạn nhập sai")   
#2 
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b + delta**1/2) / (2*a)
    x2 = (-b - delta**1/2) / (2*a)
    print("Phương trình có hai nghiệm:")
    print("x1 =", x1)
    print("x2 =", x2)
elif delta == 0:
    x = -b / (2*a)
    print("Phương trình có nghiệm kép:")
    print("x =", x)
else:
    print("Phương trình không có nghiệm thực")
#3
n=int(input("Nhập 1 số bất kì từ 1-7:"))
if n==1:
    print("1:Sunday")
elif n==2:
    print("2:Monday")
elif n==3:
    print("3:Tusday")
elif n==4:
    print("4:Wednesday")
elif n==5:
    print("5:Thursday")
elif n==6:
    print("6:Friday")
elif n==7:
    print("7:Saturday")
else:
    print("Bạn nhập ko hợp lệ..!")
#4
so = int(input("Nhập vào một số nguyên: "))

if so >= 100 and so <= 999:
    so_hang_tram = so // 100 
    print("Chữ số hàng trăm là:", so_hang_tram)
else:
    print("0")
#5
    thang = int(input("nhập tháng kiểm tra :"))
if thang ==1:
        print("January ")
elif thang == 2:
        print("February ")    
elif thang ==3:
        print("March")
elif thang ==4:
        print("April")
elif thang ==5:
        print("May")
elif thang ==6:
        print("June")
elif thang ==7:
        print("tháng có 31 ")
elif thang ==8:
        print("August")
elif thang ==9:
        print("September")
elif thang ==10:
        print("October")
elif thang ==11:
        print("November")
elif thang ==12:
        print("December")
else:
        print("bạn nhập ko hợp lệ")
#6
so1 = input("Mời nhập số nguyên: " )
so2 = input("Mời nhập số nguyên: " )
so3 = input("Mời nhập số nguyên: " )
so_nguyen_hien_co = so1+so2+so3
print("Số nguyên hiện có: ", so_nguyen_hien_co)
if so1 == "0":
    print("Không trăm", end =" ")
if so1 == "1":
    print("Một trăm", end =" ")
if so1 == "2":
    print("Hai trăm", end =" ")
if so1 == "3":
    print("Ba trăm", end =" ")
if so1 == "4":
    print("Bốn trăm", end =" ")
if so1 == "5":
    print("Năm trăm", end =" ")
if so1 == "6":
    print("Sáu trăm", end =" ")
if so1 == "7":
    print("Bảy trăm", end =" ")
if so1 == "8":
    print("Tám trăm", end =" ")
if so1 == "9":
    print("Chín trăm", end =" ")
if so2 == "0":
    print("Lẻ", end =" ")
if so2 == "1":
    print("Mười", end =" ")
if so2 == "2":
    print("Hai mươi", end =" ")
if so2 == "3":
    print("Ba mươi", end =" ")
if so2 == "4":
    print("Bốn mươi", end =" ")
if so2 == "5":
    print("Năm mươi", end =" ")
if so2 == "6":
    print("Sáu mươi", end =" ")
if so2 == "7":
    print("Bảy mươi", end =" ")
if so2 == "8":
    print("Tám mươi", end =" ")
if so2 == "9":
    print("Chín mươi", end =" ")
if so3 == "1":
    print("Mốt", end =" ")
if so3 == "2":
    print("Hai", end =" ")
if so3 == "3":
    print("Ba", end =" ")
if so3 == "4":
    print("Bốn", end =" ")
if so3 == "5":
    print("Lăm", end =" ")
if so3 == "6":
    print("Sáu", end =" ")
if so3 == "7":
    print("Bảy", end =" ")
if so3 == "8":
    print("Tám", end =" ")
if so3 == "9":
    print("Chín", end =" ")
#7
TNCT=float(input("Nhập tnct:"))
lg_cban=1350000
if TNCT>=60:
    hso=3.99
elif TNCT>=36:
    hso=3.66
elif TNCT>=12:
    hso=3.33
elif TNCT<12:
    hso=2.34
salary=hso*lg_cban
print("Lương nvien=",salary)
#8
so_kw=float(input("Nhập số kw:"))
if so_kw<=100 and so_kw>0:
    tien_dien=so_kw*2000
elif so_kw<=200:
    tien_dien=(100*2000 + (so_kw-100)*2500)
elif so_kw<=300:
    tien_dien=(100*2000 + 100*2500 + (so_kw-200)*3000)
elif so_kw>300:
    tien_dien=(100*2000 + 100*2500 + 100*3000 + (so_kw-300)*5000)
print("Cái giá phải trả:",tien_dien)
#9
gio_bat_dau = int(input("Nhập giờ bắt đầu (từ 5 đến 22): "))
gio_ket_thuc = int(input("Nhập giờ kết thúc (từ 5 đến 22): ")) 
don_gia_3_gio_dau = 100000
so_gio_thue = gio_ket_thuc - gio_bat_dau
if so_gio_thue <= 3:
    tong_tien = so_gio_thue * don_gia_3_gio_dau
else:
    tong_tien = 3 * don_gia_3_gio_dau

        # Đơn giá giảm sau 3 giờ
    don_gia_giam = don_gia_3_gio_dau - (don_gia_3_gio_dau * 0.25)

        # Tính số tiền cho các giờ tiếp theo
    tong_tien += (so_gio_thue - 3) * don_gia_giam

    # Kiểm tra giảm giá nếu thuê từ 11h đến 15h
if 11 <= gio_bat_dau <= 15:
    tong_tien *= 0.9
if 5 <= gio_bat_dau <= gio_ket_thuc <= 22:
    tien_thue_san = tong_tien
    print("Số tiền khách hàng phải trả là:", tien_thue_san, "đ")
else:
    print("Giờ không hợp lệ. Vui lòng nhập lại!")
#10
ngày = int(input("Nhập ngày: "))
tháng = int(input("Nhập tháng: "))
năm = int(input("Nhập năm: "))
if not  1 <= ngày <= 31:
    print("Ngày không hợp lệ.")
if not  1 <= tháng <= 12:
    print("Tháng không hợp lệ.")
if  năm < 0:
    print("Năm không hợp lệ.")
ngày_trong_tháng = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
ngày += 1
if ngày > ngày_trong_tháng[tháng - 1]:
    if tháng == 12:
        năm += 1
        tháng = 1
        ngày = 1
    else:
        tháng += 1
        ngày = 1
print("Ngày tiếp theo:", ngày,tháng,năm )
#11
import math
a=int(input("Nhập gtri a:"))
b=int(input("Nhập gtri b:"))
x=c=int(input("Nhập gtri c:"))
y=d=int(input("Nhập gtri d:"))
r=int(input("Nhập gtri r:"))

kcach= math.sqrt((x-a)**2 +(y-b)**2)
if kcach>r:
    print("Điểm M nằm ngoài đg tròn")
elif kcach==r:
    print("Điểm M nằm trên đg tròn")
else:
    print("Điểm M nằm trong đg tròn")
#12
x = float(input("Nhập số gam Al2O3: "))
y = float(input("Nhập nồng độ NaOH (yM): "))
z = float(input("Nhập nồng độ HCl (zM): "))

# Tính số mol của các chất
mol_Al2O3 = x / 101.96  # Khối lượng mol của Al2O3
vol_NaOH = 0.1 * y      # Thể tích NaOH sau phản ứng (100ml)
vol_HCl = 0.1 * z       # Thể tích HCl sau phản ứng (100ml)

# Số mol của NaOH và HCl trước phản ứng
mol_NaOH_trc = y * 0.1
mol_HCl_trc = z * 0.1

# Số mol của NaOH và HCl sau phản ứng
mol_NaOH_sau = mol_NaOH_trc - mol_Al2O3 / 6
mol_HCl_sau = mol_HCl_trc - mol_Al2O3 / 6

# Kiểm tra xem có kết tủa hay không
if mol_NaOH_sau < 0 or mol_HCl_sau < 0:
    print("Sau phản ứng có kết tủa.")
else:
    print("Sau phản ứng không có kết tủa.")
#13
I0 = float(input("Nhập mức cường độ âm: "))
D = float(input("Nhập khoảng cách từ nguồn phát sóng đến người nghe: "))

# Tính mức cường độ âm thanh tại vị trí người nghe
I = I0 * (1 / D)**2

if I > 100:
    print("Người nghe nghe thấy âm.")
else:
    print("Người nghe không nghe thấy âm.")
    