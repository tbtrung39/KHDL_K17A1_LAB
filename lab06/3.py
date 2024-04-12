danh_sach = []
while True:
    pt = int(input("Nhap 1 so tu nhien: "))
    if pt == 0:
        break
    danh_sach.append(pt)
print("Danh sach: ", danh_sach)

danh_sach_duong = [x for x in danh_sach if x > 0]
danh_sach_am = [x for x in danh_sach if x<= 0]
danh_sach = danh_sach_duong + danh_sach_am
print("Danh sach khi chuyen cac phan tu duong: ", danh_sach_duong)

m = int(input("Nhap m: "))
danh_sach.insert(0, m)
danh_sach.append(m)
danh_sach.insert(4, m)
print("Danh sach sau khi chen: ", danh_sach)