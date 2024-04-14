# Khởi tạo danh sách
danh_sach = []

# Nhập các số vào danh sách cho đến khi nhập số 0
while True:
    so = int(input("Nhập một số tự nhiên (nhập 0 để kết thúc): "))
    if so == 0:
        break
    danh_sach.append(so)

print("Danh sách ban đầu:", danh_sach)

# Chèn danh sách [1,2,3] vào vị trí đầu, cuối và thứ 5 của danh sách
danh_sach = [1, 2, 3] + danh_sach  # Chèn vào đầu danh sách
danh_sach += [1, 2, 3]             # Chèn vào cuối danh sách
danh_sach.insert(4, 1)             # Chèn vào vị trí thứ 5 (vị trí bắt đầu từ 0)
print("Danh sách sau khi chèn:", danh_sach)

# Xóa phần tử thứ k trong danh sách
k = int(input("Nhập vị trí phần tử cần xóa (tính từ 0): "))
if 0 <= k < len(danh_sach):
    del danh_sach[k]
    print("Danh sách sau khi xóa phần tử thứ", k, ":", danh_sach)
else:
    print("Vị trí phần tử cần xóa không hợp lệ.")

# Sắp xếp danh sách theo thứ tự tăng dần và giảm dần
danh_sach_tang_dan = sorted(danh_sach)
danh_sach_giam_dan = sorted(danh_sach, reverse=True)
print("Danh sách sau khi sắp xếp tăng dần:", danh_sach_tang_dan)
print("Danh sách sau khi sắp xếp giảm dần:", danh_sach_giam_dan)
