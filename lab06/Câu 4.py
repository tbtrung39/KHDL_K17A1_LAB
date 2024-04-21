'''
Viết chương trình nhập vào một danh sách (is) các phần từ là số tự nhiên cho đến khi nhập vào số 0.
Thực hiện các yêu cầu sau.
- Chèn danh sách [1,2,3] vào vị trí đầu, cuối và thứ 5 của danh sách.
- Xóa phần tử thứ k (k nhập từ bàn phím) trong danh sách.
- Sắp xếp danh sách theo thứ tự tăng dần, giảm dần.
'''
#Nhập danh sách số tự nhiên từ người dùng cho đến khi nhập số 0
danh_sach = []
while True:
    phan_tu = int(input("Nhập số tự nhiên (0 để kết thúc nhập): "))
    if phan_tu == 0:
        break
    danh_sach.append(phan_tu)

#Chèn danh sách [1, 2, 3] vào vị trí đầu, cuối và thứ 5 của danh sách
danh_sach = [1, 2, 3] + danh_sach
danh_sach += [1, 2, 3]
danh_sach.insert(4, 1)
print("Danh sách sau khi chèn:", danh_sach)

#Xóa phần tử thứ k
vi_tri_xoa = int(input("Nhập vị trí muốn xóa: "))
if vi_tri_xoa < len(danh_sach):
    del danh_sach[vi_tri_xoa]
    print("Danh sách sau khi xóa:", danh_sach)
else:
    print("Vị trí muốn xóa không hợp lệ.")

#Sắp xếp danh sách theo thứ tự tăng dần và giảm dần
danh_sach_tang_dan = sorted(danh_sach)
danh_sach_giam_dan = sorted(danh_sach, reverse=True)
print("Danh sách sau khi sắp xếp tăng dần:", danh_sach_tang_dan)
print("Danh sách sau khi sắp xếp giảm dần:", danh_sach_giam_dan)

