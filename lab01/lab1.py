#1
ma_so_sinh_vien = int(input("Nhập mã sinh viên là: "))
ho_ten = input("Nhập họ và tên sinh viên là:")
que_quan = input("Nhập quê quán của sinh viên là:")
nam_sinh = int(input("Nhập năm sinh của sinh viên là:"))
diem_tb_cac_nam_hoc = float(input("Nhập điểm tb các năm học của sinh viên là:"))
print(ma_so_sinh_vien,ho_ten,que_quan,nam_sinh,diem_tb_cac_nam_hoc)
#2
d = int(input("Nhập số ngày: "))
h = int(input("Nhập số giờ: "))
m = int(input("Nhập số phút: "))
s = int(input("Nhập số giây: "))
tong_so_giay = d*24*3600+h*3600+m*60 + s
print(f"{d} ngày,{h} giờ,{m} phút,{s} giây tương đương với {tong_so_giay} giây.")
#3
chieu_cao = int(input("Nhap chieu cao la:"))
ban_kinh = int(input("Nhap ban kinh la:"))
pi=3.14
dt_xung_quanh = 2*pi*ban_kinh*chieu_cao
dt_xung_quanh = round(dt_xung_quanh,2)
dt_toan_phan = dt_xung_quanh + 2*pi*(ban_kinh**2)
dt_toan_phan = round(dt_toan_phan,2)
the_tich = pi*(ban_kinh**2)*chieu_cao
the_tich = round(the_tich,2)
print("Dien tich xung quanh la:",dt_xung_quanh)
print("Dien tich toan phan la:",dt_toan_phan)
print("The tich la:",the_tich)
#4
import math
x = int(input("Nhap gia tri x la:"))
f = (-x + math.sqrt(x**2+4)) / (x**4+1)**(1/7)
f = round(f,2)
print("Bieu thuc f(x) la:",f)
#5
a1 = int(input("Nhap toa do vecto a1 la:"))
a2 = int(input("Nhap toa do vecto a2 la:"))
b1 = int(input("Nhap toa do vecto b1 la:"))
b2 = int(input("Nhap toa do vecto b2 la:"))
T = a1*b1 + a2*b2
print("Tich vo huong la:",T)
#6
t = int(input(" nhap thoi gian : "))
cong_suat_tieu_thu= 220*2.7*t
so_tien_phai_tra= cong_suat_tieu_thu*(7000/3600000)
print("so tien phai tra la :",so_tien_phai_tra)
#7
a = int(input("Nhap gia tri a la:"))
b = int(input("Nhap gia tri b la:"))
c = int(input("Nhap gia tri c la:"))
x = -b / (2*a) 
y = a*(x**2) + b*x + c
x = round(x,2)
y = round(y,2)
print("Dinh cua phuong trinh bac 2 la:",(x,y))
#8
xa = int(input("nhập vào tọa độ xa: "))
ya = int(input("nhập vào tọa độ ya: "))
xb = int(input("nhập vào tọa độ xb: "))
yb = int(input("nhập vào tọa độ yb: "))
xc = int(input("nhập vào tọa độ xc: "))
yc = int(input("nhập vào tọa độ yc: "))
xg = (xa + xb + xc)/3
yg = (ya + yb + yc)/3
xg = round(xg,2)
yg = round(yg,2)
print("Trong tam cua tam giac la:",(xg,yg))
#9
x = int(input("Toa do x la:"))
y = int(input("Toa do y la:"))
z = int(input("Toa do z la:"))
print("tọa độ của điểm đối xứng với nó qua mặt phẳng Oxy la:",(x,y,-z))
print("tọa độ của điểm đối xứng với nó qua mặt phẳng Oxz la:",(x,-y,z))
print("tọa độ của điểm đối xứng với nó qua mặt phẳng Oyz la:",(-x,y,z))
#10
import math
x = int(input('Nhap gia tri x la:'))
f = math.log(x,4) + math.log(2,x)
f = round (f,2)
print("Gia tri cua bieu thuc f(x) la:",f)
#11
n = int(input("nhập vào số lần tung xúc sắc: "))
p = (1/6)**3
q = (1-p)**n
xx = 1 - q
print(f"xác suất số lần ra 3 con 6 khi tung {n} lần xúc sắc = {xx:.2f}")