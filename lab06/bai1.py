#câu 1
#ý thứ nhất
a = [2,-4,1,9,-3,6,3,-2,6,8]
tong = 0
for i in a:
    tong += i
print(f"tổng các phần tử của danh sách là:{tong}")
#ý thứ 2
so_hang_duong = []
for i in a:
    if i > 0:
        so_hang_duong.append(i)
print(f"các số hạng dương là:{so_hang_duong}")
#ý thứ 3
for i in a:
    if i < 0:
        break
print(f"phần tử âm đầu tiên là:{i}")
#ý thứ 4
for i in a:
    if i > 0:
        so_hang_duong_cuoi_cung = []
        so_hang_duong_cuoi_cung.append(i)
print(f"các số hạng dương là:{so_hang_duong_cuoi_cung}")
#ý thứ 5
print(f"phần tử lớn nhất của danh sách là:{max(a)}")
#cách 2
a.sort()
print(f"phần tử lớn nhất của danh sách là:{a[9]}")