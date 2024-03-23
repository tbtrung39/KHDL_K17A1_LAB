import math
r = int(input("Nhập bán kính: "))
h = int(input("Nhập chiều cao: "))

dien_tich_xung_quanh = 2*3.14*r*h
dien_tich_toan_phan = 3.14*r*(r+h)
the_tich = 3.14*(r**2)*h

Sxq = round(dien_tich_xung_quanh, ndigits= 2)
Stp = round(dien_tich_toan_phan, ndigits=2)
V = round(the_tich, ndigits=2)

print("Diện tích xung quanh:",Sxq)
print("Diện tích toàn phần: ", Stp)
print("Thể tích khối trụ: ", V)