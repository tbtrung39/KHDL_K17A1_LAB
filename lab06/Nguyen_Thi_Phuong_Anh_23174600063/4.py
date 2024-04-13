danh_sach = []
phan_tu = input("Nhập vào một số tự nhiên hoặc 'o' để kết thúc: ")

while phan_tu != 'o':
    if phan_tu.isdigit():
        danh_sach.append(int(phan_tu))
    else:
        print("Vui lòng chỉ nhập số tự nhiên.")
    phan_tu = input()
print("Danh sách ban đầu:", danh_sach)
danh_sach.insert(0, [1,2,3])
danh_sach.append({1,2,3})
danh_sach.insert(4,{1,2,3})
print("Danh sách sau khi chèn:", danh_sach)

k = input("Nhập vị trí muốn xóa (k): ")
if k.isdigit() and 0 <= int(k) < len(danh_sach):
    danh_sach = danh_sach[:int(k)] + danh_sach[int(k)+1:]
    print("Danh sách sau khi xóa phần tử thứ", k, ":", danh_sach)
else:
    print("Vị trí không hợp lệ.")

danh_sach_tang = sorted(danh_sach)
print("Danh sách sau khi sắp xếp tăng dần là:",danh_sach_tang)

danh_sach_giam = sorted(danh_sach, reverse=True)
print("Danh sách sau khi sắp xếp theo thứ tự giảm dàn là:",danh_sach_giam)