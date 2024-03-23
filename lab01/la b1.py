#1
bkinh =float(input("Nhap ban kinh: "))
ccao =float(input("Nhap chieu cao:"))
#Tinh the tich
V= 3.14*(bkinh**2)*ccao
#Tinh dien tich toan phan
Stp= 2*3.14*bkinh*ccao +2*3.14*(bkinh**2)
#Tinh dien tich xung quanh
Sxq= 2*3.14*bkinh*ccao
print(f"The tich={V:.2f}, Dien tich tp={Stp:.2f},Dien tich xq={Sxq:.2f}")
#2
import math
x= float(input("Nhập gtri x:"))
#Gtri biểu thức 
Fx= (-x+math.sqrt(x**2 +4))/((7**0.5)*(x**4)+1)
print(f"Gtri bthuc={Fx:.2f}")
#3
x1=float(input("Nhập gtri x1:"))
y1=float(input("Nhập gtri y1:"))
x2=float(input("Nhập gtri x2:"))
y2=float(input("Nhập gtri y2:"))
 #Tích vố hướng 
tvh=x1*y1+x2*y2
print("Tích vô hướng=",tvh)
#4
t=float(input("Nhập tgian sd:"))
so_dien=220*2.7*(t/3600000)
tien_phai_tra=so_dien*7000
print("Tiền cần nộp:",tien_phai_tra)     
#6
x1=float(input("Nhập gtri x1:"))
y1=float(input("Nhập gtri y1:"))
x2=float(input("Nhập gtri x2:"))
y2=float(input("Nhập gtri y2:"))
x3=float(input("Nhập gtri x3:"))
y3=float(input("Nhập gtri y3:"))
#Tính tọa độ đỉnh
dinh_x=(x1+x2+x3)/3
dinh_y=(y1+y2+y3)/3
print(f"Tọa độ đỉnh x={dinh_x:.2f}")
print(f"Tọa độ đỉnh y={dinh_y:.2f}")
#7
x=int(input("Nhập x:"))
y=int(input("Nhập y:"))
z=int(input("Nhập z:"))
dxung_Oyz=(-x,y,z)
dxung_Oxz=(x,-y,z)
dxung_Oxy= (x,y,-z)
print("dxung qua Oxy:",dxung_Oxy)
print("dxung qua Oxz:", dxung_Oxz)
print("dxung qua Oyz:", dxung_Oyz)
#8
import math
x=float(input("Nhập gtri x:"))
 
Fx=math.log(x,4)+ math.log(2,x)
print(F"Gtri bthuc={Fx:.2f}")
#9
n=int(input("Nhập số lần tung:"))
#Tổng số lần ra full 6
full=6**n
#Tổng số lần ra ko có 6
not6=5**n
#Xác suất ko có 6
xs=not6/full 
#Xác suất 1 lần ra 6
xs6=1-xs
print(f"Xác suất có 1 lần cả 3 ra 6={xs6:.2f}")