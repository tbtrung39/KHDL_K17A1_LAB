n = int(input("Số phần tử danh sách: "))
danh_sach = []
for i in range(n):
    pt = int(input(f"Nhập phần tử thứ {i+1}: "))
    danh_sach.append(pt)
print(danh_sach)
print(f"danh sách sau khi kết thúc chương trình {danh_sach}")
#a
ds_moi = sorted(danh_sach,reverse=True)
b = ds_moi[1]
print(f"phần tử lớn thứ 2 là {ds_moi[1]}")
print(f"vị trí phần tử lớn thứ 2 là {danh_sach.index(b)}")
#b
danh_sach.append(int(n))
slsd_max = 0
slsd_now = 0
for num in danh_sach:
    if num > 0:
        slsd_now += 1
        slsd_max = max(slsd_max, slsd_now)
    else:
        slsd_now = 0
print(f"Số lượng số dương liên tiếp nhiều nhất là: {slsd_max}")