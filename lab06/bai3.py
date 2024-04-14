danh_sach = []
while True:
    so = int(input("Nhập số tự nhiên (nhập 0 để kết thúc): "))
    if so == 0:
        break
    danh_sach.append(so)
print("Danh sách ban đầu:", danh_sach)
duong = [x for x in danh_sach if x > 0]
for x in duong:
    danh_sach.remove(x)
danh_sach[:0] = duong
print("Danh sách sau khi chuyển các số dương lên đầu:", danh_sach)
m = int(input("Nhập số m để chèn vào đầu, cuối và vị trí thứ 5 của danh sách: "))
danh_sach.insert(0, m)  
print("Danh sách sau khi chèn số", m, "vào đầu:", danh_sach)
danh_sach.append(m)  
print("Danh sách sau khi chèn số", m, "vào cuối:", danh_sach)
danh_sach.insert(4, m)  
print("Danh sách sau khi chèn số", m, "vào vị trí thứ 5:", danh_sach)
