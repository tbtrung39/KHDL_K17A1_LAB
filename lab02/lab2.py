#1.Viết chương trình nhập vào một tháng và cho biết tháng đó có bao nhiêu ngày.
thang = int(input("Mời nhập tháng cần kiểm tra: "))
if thang >=1 and thang <= 12:
    if thang == 1:
        print("Tháng này có 31 ngày")
    if thang == 2: 
        print("Tháng này có 30 ngày")
    if thang == 3: 
        print("Tháng này có 31 ngày")
    if thang == 4: 
        print("Tháng này có 30 ngày")
    if thang == 5: 
        print("Tháng này có 30 ngày")
    if thang == 6: 
        print("Tháng này có 30 ngày")
    if thang == 7: 
        print("Tháng này có 30 ngày")
    if thang == 8: 
        print("Tháng này có 30 ngày")
    if thang == 9: 
        print("Tháng này có 30 ngày")
    if thang == 10: 
        print("Tháng này có 30 ngày")
    if thang == 11: 
        print("Tháng này có 30 ngày")
    if thang == 12: 
        print("Tháng này có 30 ngày")
else: 
    print("Tháng nhập vào không hợp lệ")

#2. Viết chương trình nhập vào các hệ số a, b, c và in ra nghiệm của phương trình bậc hai ax^2+ bx + c = 0 
a = int(input("Mời nhập hệ số a: "))
b = int(input("Mời nhập hệ số b: "))
c = int(input("Mời nhập hệ số c: "))
delta = b*b-4*a*c
if delta > 0:
    x1 = (-b + (delta**(1/2)))/(2*a)
    x2 = (-b - (delta**(1/2)))/(2*a)
    print("Nghiệm của phương trình là: ", x1, "và", x2)
elif delta == 0:
    print("Phương trình có nghiệm kép: ",(-b)/(2*a))
else: 
    print("Phương trình vô nghiệm")

#3. Viết chương trình cho phép nhập vào thứ (1->7) trong tuần. Sau đó cho biết thứ đã nhập có tên là gì và xuất kết quả ra màn hình. (1: Sunday, 2: Monday, …)
thu = int(input("Mời nhập thứ muốn biết: "))
if thu >=1 and thu <= 7:
    if thu == 1:
        print("Sunday")
    if thu == 2:
        print("Monday")
    if thu == 3:
        print("Tuesday")
    if thu == 4:
        print("Wednesday")
    if thu == 5:
        print("Thursday")
    if thu == 6:
        print("Friday")
    if thu == 7:
        print("Staturday")
else:
    print("Thứ nhập vào không hợp lệ")   

#4. Nhập vào 1 số nguyên, yêu cầu xuất ra chữ số hàng trăm của số đó, nếu không có thì xuất ra 0.
so = int(input("Mời nhập 1 số: "))
if so < 100:
    print(0)
if so >= 100 and so < 200:
    print(1)
if so >= 200 and so < 300:
    print(2)
if so >= 300 and so < 400:
    print(3)
if so >= 400 and so < 500:
    print(4)
if so >= 500 and so < 600:
    print(5)
if so >= 600 and so < 700:
    print(6)
if so >= 700 and so < 800:
    print(7)
if so >= 800 and so < 900:
    print(8)
if so >= 900 and so < 1000:
    print(9)

#5. Viết chương trình cho phép nhập vào tháng (1->12) trong năm. Sau đó cho biết tháng đó có tên là gì và xuất kết quả ra màn hình. (1: January, 2: February, …)
thang = int(input("Mời nhập tháng: "))
if thang >=1 and thang <= 12:
    if thang == 1:
        print('January')
    if thang == 2:
        print('February')
    if thang == 3:
        print('March')
    if thang == 4:
        print('April')
    if thang == 5:
        print("May")
    if thang == 6:
        print("June")
    if thang == 7:
        print("July")
    if thang == 8:
        print("August")
    if thang == 9:
        print("September")
    if thang == 10:
        print("October")
    if thang == 11:
        print("November")
    if thang == 12:
        print("December")
else:
    print("Tháng nhập vào không hợp lệ")

#6. Viết chương trình nhập vào một số nguyên có ba chữ số. Hãy in ra cách đọc của số nguyên này.
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

#7. 
diem_TK = float(input("Mời nhập điểm tổng kết: "))
if diem_TK >= 0.0 and diem_TK < 3.0:
    print("Xếp loại kém")
if diem_TK >= 3.0 and diem_TK <5:
    print("Xếp loại yếu")
if diem_TK >= 5.0 and diem_TK <7:
    print("Xếp loại trung bình")
if diem_TK >= 7 and diem_TK < 8:
    print("Loại khá")
if diem_TK >= 8 and diem_TK < 9.0:
    print("Xếp loại giỏi")
if diem_TK >= 9 and diem_TK <= 10:
    print("Xếp loại Xuất Xắc")

#8. Viết chương trình tính lương của nhân viên dựa theo thâm niên công tác (TNCT) như sau: Lương = hệ số * lương căn bản, trong đó lương căn bản là 1350000 đồng.
TNCT = int(input("Nhập thâm niên công tác: "))
if TNCT < 0:
    print("TNCT không hợp lệ")
if TNCT< 12:
    he_so = 2.34
if TNCT >= 12 and TNCT < 36:
    he_so = 3.33
if TNCT >= 36 and TNCT < 60:
    he_so = 3.66
if TNCT >= 60:
    he_so = 3.99
luong_CB = 1350000
luong = he_so*luong_CB
print("Lương nhân viên là: ", luong)

#9. Viết chương trình cho phép nhập số KW điện tiêu thụ từ bàn phím. Sau đó tính tiền điện và xuất kết quả ra màn hình.
kw = int(input("Nhập số KW tiêu thụ: "))
if kw <= 100:
    price = 2000
elif kw <= 200:
    price = 2500
elif kw <= 300:
    price = 3000
else:
    price = 5000
print(f"Tổng tiền điện là: {kw*price} đồng")

#10.Một điểm cho thuê sân tập bóng đá theo công thức sau:
# Mỗi giờ trong 03 giờ đầu tiên tính 100000đ/giờ
# Mỗi giờ tiếp theo có đơn giá giảm 25% so với đơn giá trong 3 giờ đầu tiên.
# Ngoài ra nếu thời gian thuê sân từ 11 giờ đến 15 giờ thì được giảm giá 10%.
#Viết chương trình nhập vào giờ bắt đầu, giờ kết thúc và in ra số tiền khách thuê sân tập phải trả, biết rằng 5 giờ <= giờ bắt đầu <= giờ kết thúc <= 22 giờ
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

#11. Cho trước số ngày trong một tháng của năm không nhuận như sau
#Tháng 1 có 31 ngày
#Tháng 2 có 28 ngày
#Tháng 3 có 31 ngày
#Tháng 4 có 30 ngày
#Tháng 5 có 31 ngày
#Tháng 6 có 30 ngày
#Tháng 7 có 31 ngày
#Tháng 8 có 31 ngày
#Tháng 9 có 30 ngày
#Tháng 10 có 31 ngày
#Tháng 11 có 30 ngày
#Tháng 12 có 31 ngày
#Hãy viết chương trình xuất ra ngày tiếp theo của 1 ngày cho trước.
# Nhập ngày, tháng, năm từ người dùng
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

# Kiểm tra năm nhuận
is_nam_nhuan = (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)

# Kiểm tra số ngày của tháng
if thang == 2:
    if is_nam_nhuan:
        so_ngay_trong_thang = 29
    else:
        so_ngay_trong_thang = 28
elif thang in [4, 6, 9, 11]:
    so_ngay_trong_thang = 30
else:
    so_ngay_trong_thang = 31

# Kiểm tra và tính ngày tiếp theo
if 1 <= ngay <= so_ngay_trong_thang:
    if ngay < so_ngay_trong_thang:
        ngay_tiep_theo = ngay + 1
        thang_tiep_theo = thang
        nam_tiep_theo = nam
    else:
        ngay_tiep_theo = 1
        thang_tiep_theo = thang + 1
        nam_tiep_theo = nam

        if thang_tiep_theo > 12:
            thang_tiep_theo = 1
            nam_tiep_theo += 1

    print(f"Ngày tiếp theo là: {ngay_tiep_theo}/{thang_tiep_theo}/{nam_tiep_theo}")
else:
    print("Ngày không hợp lệ.")

#12. Phương trình đường tròn có dạng:
#(x - a)^2 + (y - b)^2 = r^2
#và điểm M(c,d) bất kì 
#Nhập vào từ bàn phím a,b,c,d, và r. Xác định vị trí của điểm M so với đường tròn
import math
a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
c = float(input("Nhập giá trị c: "))
d = float(input("Nhập giá trị d: "))
r = float(input("Nhập giá trị r: "))
khoang_cach = math.sqrt((c - a)**2 + (d - b)**2)
if khoang_cach < r:
    print("Điểm M nằm trong đường tròn.")
elif khoang_cach == r:
    print("Điểm M nằm trên đường tròn.")
else:
    print("Điểm M nằm ngoài đường tròn.")

#13. Cho x gam Al2O3 vào 100ml dung dịch NaOH yM, sau phản ứng cho thêm 100ml dung dịch HCL zM. Biết x, y, z được nhập từ bàn phím. Xác định sau phản ứng có kết tủa hay không?
# Nhập liệu từ bàn phím
x = float(input("Nhập số gam Al2O3: "))
y = float(input("Nhập nồng độ NaOH (yM): "))
z = float(input("Nhập nồng độ HCl (zM): "))

# Tính số mol của các chất
mol_Al2O3 = x / 101.96  # Khối lượng mol của Al2O3
vol_NaOH = 0.1 * y      # Thể tích NaOH sau phản ứng (100ml)
vol_HCl = 0.1 * z       # Thể tích HCl sau phản ứng (100ml)

# Số mol của NaOH và HCl trước phản ứng
mol_NaOH_before = y * 0.1
mol_HCl_before = z * 0.1

# Số mol của NaOH và HCl sau phản ứng
mol_NaOH_after = mol_NaOH_before - mol_Al2O3 / 6
mol_HCl_after = mol_HCl_before - mol_Al2O3 / 6

# Kiểm tra xem có kết tủa hay không
if mol_NaOH_after < 0 or mol_HCl_after < 0:
    print("Sau phản ứng có kết tủa.")
else:
    print("Sau phản ứng không có kết tủa.")
    