danh_sach = []
while True:
    pt = int(input("nhập 1 số tự nhiên:"))
    if pt == 0:
        break
    danh_sach.append(pt)
print("Danh sách; ", danh_sach)

danh_sach_duong = [x for x in danh_sach if x > 0]
danh_sach_am = [x for x in danh_sach if x <= 0]
danh_sach = danh_sach_duong + danh_sach_am
print("Danh sách khi chuyển các phần tử dương: ", danh_sach_duong)

m = int(input("Nhập m: "))
danh_sach.insert(0, m)
danh_sach.append(m)
danh_sach.insert(4, m)
print("danh sách sau khi chèn: ", danh_sach)