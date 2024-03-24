import math

r = float(input("Nhập bán kính của khối trụ: "))
h = float(input("Nhập chiều cao của khối trụ: "))

surface_area = 2 * math.pi * r * h
total_area = 2 * math.pi * r * (r + h)
volume = math.pi * r ** 2 * h

print("Diện tích xung quanh của khối trụ:", round(surface_area, 2))
print("Diện tích toàn phần của khối trụ:", round(total_area, 2))
print("Thể tích của khối trụ:", round(volume, 2))
