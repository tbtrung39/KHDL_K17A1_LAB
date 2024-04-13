danh_sach = []
while True:
    phan_tu = int(input("Nhập phần tử (nhập 0 để kết thúc): "))
    if phan_tu == 0:
        break
    danh_sach.append(phan_tu)
print(danh_sach)
danh_sach_tang_dan = sorted(danh_sach)
danh_sach_giam_dan = sorted(danh_sach,reverse=True)
print("Danh sách sau khi sắp xếp tăng dần: ",danh_sach_tang_dan)
print("Danh sách sau khi sắp xếp giảm dần: ",danh_sach_giam_dan)

danh_sach.insert(0,[1,2,3])
danh_sach.append([1,2,3])
danh_sach.insert(5,[1,2,3])
print("Danh sách sau khi chèn: ",danh_sach)

k = int(input("Xoá phần tử thứ: "))
danh_sach.remove(k)
print(f"Danh sách sau khi xoá phần tử thứ {k}: ",danh_sach)