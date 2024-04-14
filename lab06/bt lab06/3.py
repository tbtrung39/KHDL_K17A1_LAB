danh_sach = []
while True:
    so = int(input("Nhập một số tự nhiên (nhập 0 để kết thúc): "))
    if so == 0:
        break
    danh_sach.append(so)
print("Danh sách ban đầu:", danh_sach)
so_duong = [so for so in danh_sach if so > 0]
so_con_lai = [so for so in danh_sach if so <= 0]
danh_sach = so_duong + so_con_lai
print("Danh sách sau khi chuyển các số dương lên đầu:", danh_sach)
m = int(input("Nhập số m: "))
danh_sach.insert(0, m)  
danh_sach.append(m)     
danh_sach.insert(4, m)  
print("Danh sách sau khi chèn số m:", danh_sach)
