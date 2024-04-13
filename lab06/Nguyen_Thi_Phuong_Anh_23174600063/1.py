a = [2,-4,1,9,-3,6,8]

# tính các phần tử trong list
print("Tổng các phần tử của danh sách :",sum(a))

# đếm số lượng các số hạng dương và tổng các số hạng dương'
so_luong_duong = 0
tong_duong = 0
for num in a :
    so_luong_duong += 1
    tong_duong += num
print("Số lượng các số dương là:", so_luong_duong)
print("Tổng các số dương là:",tong_duong)

#tìm vị trí của phần tử âm đầu tiên trong danh sách
thay_am = False
first_am = -1
for i in range(len(a)):
    if a[i] < 0:
        thay_am = True
        first_am = i
        break
if thay_am:
    print("Vị trí của phần tử âm đầu tiên trong danh sách là:", first_am)
else:
    print("không có phần tử âm trong danh sách")

#vị trí phần tử dương cuối cùng
thay_duong = False
last_duong = -1
for i in range(len(a)):
    if a[i] > 0:
        thay_duong = True
        last_duong = i

if thay_duong:
    print("Vị trí phần tử dương cuối cùng là:", last_duong)
else:
    print("Không có phần tử dương trong danh sách.")

# tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng

phan_tu_max = max(a)
vi_tri_max = a.index(phan_tu_max)
print("Phần tử lớn nhất trong list là:",phan_tu_max)
print("Vị trí phần tử max của list là:", vi_tri_max)
    



























































