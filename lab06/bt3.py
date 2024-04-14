# Khởi tạo danh sách
danh_sach = []

# Nhập các số vào danh sách cho đến khi nhập số 0
while True:
    so = int(input("Nhập một số tự nhiên (nhập 0 để kết thúc): "))
    if so == 0:
        break
    danh_sach.append(so)

print("Danh sách ban đầu:", danh_sach)

# Chuyển các số dương lên đầu danh sách
so_duong = [so for so in danh_sach if so > 0]
so_con_lai = [so for so in danh_sach if so <= 0]
danh_sach = so_duong + so_con_lai
print("Danh sách sau khi chuyển các số dương lên đầu:", danh_sach)

# Nhập số m từ bàn phím
m = int(input("Nhập số m: "))

# Chèn số m vào đầu, cuối và vị trí thứ 5 của danh sách
danh_sach.insert(0, m)  # Chèn vào đầu danh sách
danh_sach.append(m)     # Chèn vào cuối danh sách
danh_sach.insert(4, m)  # Chèn vào vị trí thứ 5 (vị trí bắt đầu từ 0)
print("Danh sách sau khi chèn số m:", danh_sach)
