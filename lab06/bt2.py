n = int(input("Nhập vào số tự nhiên n: "))
list = []
#nhập danh sách
for i in range(n):
    num = int(input(f"Nhập phần tử thứ {i+1}: "))
    list.append(num)
print(list)
#tìm phần tử lón thứ 2
#bằng cách tìm phần tử lớn nhất rồi xoá phần tử đó đi tìm phần tử lớn nhất tiếp theo của list
list_a = list.copy()
max1 = max(list_a)
list_a.remove(max1)
max2 = max(list_a)
vi_tri_max_thu_hai = list_a.index(max2)
print(f"vi tri cua phan tu lon thu hai la {vi_tri_max_thu_hai}")
#tính số lượng các số dương liên tiếp nhiều nhất
so_luong_lon_nhat = 0
so_luong_hien_tai = 0
for i in list:
    if i > 0:
        so_luong_hien_tai += 1
    else:
        so_luong_hien_tai = 0
o_luong_lon_nhat = max(so_luong_lon_nhat, so_luong_hien_tai)
print("Số lượng các số dương liên tiếp nhiều nhất là:", so_luong_lon_nhat)
# Tính số lượng các số dương liên tiếp có tổng lớn nhất
tong_gia_tri_max = 0
tong_hien_tai = 0
for num in list:
    if num > 0:
        tong_hien_tai += num
        tong_gia_tri_max = max(tong_gia_tri_max, tong_hien_tai)
    else:
        tong_hien_tai = 0

print("Số lượng các số dương liên tiếp có tổng lớn nhất là:", tong_gia_tri_max)
