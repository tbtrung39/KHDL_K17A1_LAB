# câu 1

msv = input("Nhập mã số sinh viên: ")
full_name = input("Nhập họ và tên: ")
hometown = input("Nhập quê quán: ")
birth_year = input("Nhập năm sinh: ")
gpa = float(input("Nhập điểm trung bình: "))

print("\nThông tin sinh viên:")
print("Mã số sinh viên:", msv)
print("Họ và tên:", full_name)
print("Quê quán:", hometown)
print("Năm sinh:", birth_year)
print("Điểm trung bình:", gpa)

# câu 2
print("2. Đổi giá trị thời gian")
s = int(input("Nhập số giây: "))
m = int(input("Nhập số phút: "))
h = int(input("Nhập số giờ: "))
d = int(input("Nhập số ngày: "))

sum_s = d * 24 * 3600 + h * 3600 + m * 60 + s
print(f"{d} ngày, {h} giờ, {m} phút, {s} giây tương ứng là {sum_s} giây.")
 
# câu 3 
import math

r = float(input("Nhập bán kính của khối trụ: "))
h = float(input("Nhập chiều cao của khối trụ: "))

surface_area = 2 * math.pi * r * h
total_area = 2 * math.pi * r * (r + h)
volume = math.pi * r ** 2 * h

print("Diện tích xung quanh của khối trụ:", round(surface_area, 2))
print("Diện tích toàn phần của khối trụ:", round(total_area, 2))
print("Thể tích của khối trụ:", round(volume, 2))

# câu 4
import math

x = float(input("Nhập giá trị của x: "))

numerator = -x + math.sqrt(x ** 2 + 4)
denominator = (x ** 4 + 17)** (1/7)

result = numerator / denominator
print("Giá trị của biểu thức là:", round(result, 2))

# câu 5
a1 = float(input("Nhập phần tử thứ 1 của vector a: "))
a2 = float(input("Nhập phần tử thứ 2 của vector a: "))

b1 = float(input("Nhập phần tử thứ 1 của vector b: "))
b2 = float(input("Nhập phần tử thứ 2 của vector b: "))

tich = a1 * b1 + a2 * b2
print("Tích vô hướng của 2 vector là:", round(tich, 2))
 # câu 6

time_use = int(input("Nhập thời gian sử dụng bóng đèn (giây): "))
a = 7000
b = (220 * 2.7 * time_use) / (1000 * 3600)
_money = b * a
print("Tiền điện phải trả:", round(_money, 2), "VNĐ")

# câu 7
a = float(input("Nhập giá trị của a: "))
b = float(input("Nhập giá trị của b: "))
c = float(input("Nhập giá trị của c: "))


x = -b / (2 * a)


y = a * x**2 + b * x + c

print("Tọa độ của đỉnh là: (", round(x, 2), ",", round(y, 2), ")")

# câu 8
# Nhập tọa độ của 3 đỉnh A, B, C của tam giác
Ax = float(input("Nhập tọa độ x của điểm A: "))
Ay = float(input("Nhập tọa độ y của điểm A: "))

Bx = float(input("Nhập tọa độ x của điểm B: "))
By = float(input("Nhập tọa độ y của điểm B: "))

Cx = float(input("Nhập tọa độ x của điểm C: "))
Cy = float(input("Nhập tọa độ y của điểm C: "))


Tx = (Ax + Bx + Cx) / 3
Ty = (Ay + By + Cy) / 3

print("Tọa độ của trọng tâm là: (", round(Tx, 2), ",", round(Ty, 2), ")")
# câu 9

x = float(input("Nhập tọa độ x của điểm: "))
y = float(input("Nhập tọa độ y của điểm: "))
z = float(input("Nhập tọa độ z của điểm: "))

#  mặt phẳng Oxy
x_xy = x
y_xy = y
z_xy = -z

# Tính tọa độ của điểm đối xứng qua mặt phẳng Oxz
x_xz = x
y_xz = -y
z_xz = z

# Tính tọa độ của điểm đối xứng qua mặt phẳng Oyz
x_yz = -x
y_yz = y
z_yz = z

# In kết quả
print("Tọa độ của điểm đối xứng qua mặt phẳng Oxy:", (x_xy, y_xy, z_xy))
print("Tọa độ của điểm đối xứng qua mặt phẳng Oxz:", (x_xz, y_xz, z_xz))
print("Tọa độ của điểm đối xứng qua mặt phẳng Oyz:", (x_yz, y_yz, z_yz))
