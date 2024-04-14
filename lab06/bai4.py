danh_sach = []

while True:
    so = int(input("Nhập số tự nhiên (nhập 0 để kết thúc): "))
    if so == 0:
        break
    danh_sach.append(so)

print("Danh sách ban đầu:", danh_sach)

danh_sach[:0] = [1, 2, 3]  
print("Danh sách sau khi chèn vào đầu:", danh_sach)

danh_sach.extend([1, 2, 3])  
print("Danh sách sau khi chèn vào cuối:", danh_sach)

danh_sach.insert(4, 1)  
danh_sach.insert(5, 2)
danh_sach.insert(6, 3)
print("Danh sách sau khi chèn vào vị trí thứ 5:", danh_sach)

k = int(input("Nhập vị trí phần tử cần xóa: "))
if 0 <= k < len(danh_sach):
    del danh_sach[k]
    print("Danh sách sau khi xóa phần tử thứ", k, ":", danh_sach)
else:
    print("Vị trí không hợp lệ.")

danh_sach_tang_dan = sorted(danh_sach)
print("Danh sách sau khi sắp xếp tăng dần:", danh_sach_tang_dan)

danh_sach_giam_dan = sorted(danh_sach, reverse=True)
print("Danh sách sau khi sắp xếp giảm dần:", danh_sach_giam_dan)
