n = int(input("Nhập n:"))
list = []
# viết chuong trình tìm phần tử lớn thứ 2 của danh sách và vị trí của phần tử đtạ giá trị lớn thứ 2
for i in range(n):
    phan_tu = int(input(f"Nhập phần tử thứ {i+1}:"))
    list.append(phan_tu)
list.sort()
max_th2 = list[-2]
vi_tri_max_th2 = list.index(max_th2)

print("Phần tử lớn thứ 2:",max_th2)
print("Vị trí phần tử lớn thứ 2:",vi_tri_max_th2)

# tính số lượng các số dươn liên tiếp nhiều nhất
max_so_luong = 0
so_luong_hien_tai = 0
for so in list:
    if so > 0:
        so_luong_hien_tai += 1
        max_so_luong = max(max_so_luong,so_luong_hien_tai)
    else:
        so_luong_hien_tai = 0
    print("Số lượng các số dương liên tiếp nhiều nhất là:",max_so_luong)

# tính số lượng các số dương liên tiếp có tổng lớn nhất

