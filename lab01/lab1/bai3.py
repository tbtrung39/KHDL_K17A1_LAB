import math

r = float(input("Nhập bán kính của khối trụ: "))
h = float(input("Nhập chiều cao của khối trụ: "))

dien_tich_xung_quanh = 2 * math.pi * r * h
dien_tich_toan_phan = 2 * math.pi * r * (r + h)
the_tich = math.pi * (r**2) * h

print("Diện tích xung quanh của khối trụ:", round(dien_tich_xung_quanh, 2))
print("Diện tích toàn phần của khối trụ:", round(dien_tich_toan_phan, 2))
print("Thể tích của khối trụ:", round(the_tich, 2))
