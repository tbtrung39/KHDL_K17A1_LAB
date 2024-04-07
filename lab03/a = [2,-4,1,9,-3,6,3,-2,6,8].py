#cau 1
a = [2,4,1,9,-3,6,3,-2,6,8]
sum = 0
dem = 0
for i in a:
    if i > 0:
        dem += 1
        sum += i
print(dem)
print(sum)
#c
def tim_vi_tri_am_dau_tien(lst):
    for i, num in enumerate(lst):
        if num < 0:
            return i
    return -1  

# \
lst = [1, 2, -3, 4, -5]
vi_tri_am_dau_tien = tim_vi_tri_am_dau_tien(lst)

if vi_tri_am_dau_tien != -1:
    print("Vị trí của phần tử âm đầu tiên trong list là:", vi_tri_am_dau_tien)
else:
    print("Không có phần tử âm trong list.")
#d 
a = [1,4,5,-2,-6,1,-,9,4,8]
for i in a:
    if i > 0 :
        continue
print(i)
#e 
a = [1,2,3-4,-6,1,-6,1,-9]
max_element = max(a) # tìm phần tử lớn nhất của danh sách
last_index = len(a) - 1 - a[::-1].index(max_element) # tìm vị trí cuối cùng của phần tử lớn nhất
print("phần tử lớn nhất của danh sách là", max_element)
print("vị trí cuối cùng của phần từ lownsn nhất là", last_index)
# CÂU 2
n = int(input("Nhập số lượng phần tử trong danh sách: "))
arr = []

for i in range(n):
    num = int(input(f"Nhập phần tử thứ {i+1}: "))
    arr.append(num)

max_num = max(arr)
second_max = float('-inf')
for num in arr:
    if num != max_num and num > second_max:
        second_max = num
second_max_index = arr.index(second_max)

max_count = 0
current_count = 0
for num in arr:
    if num > 0:
        current_count += 1
        max_count = max(max_count, current_count)
    else:
        current_count = 0

max_sum = 0
current_sum = 0
for num in arr:
    if num > 0:
        current_sum += num
        max_sum = max(max_sum, current_sum)
    else:
        current_sum = 0

print(f"Phần tử lớn thứ hai là {second_max} ở vị trí {second_max_index}")
print(f"Số lượng số dương liên tiếp nhiều nhất là: {max_count}")
print(f"Tổng số dương liên tiếp lớn nhất là: {max_sum}")
# câu 10     
import random 
cac_so_chia_het_cho_5_va_7 = [ so for so in range(201) if so % 5 == 0 and so % 7 == 0]
so_ngau_nhien = random.choice(cac_so_chia_het_cho_5_va_7)
print("so ngau nhien chia het cho 5 va 7", so_ngau_nhien)
# câu 13
chu_ngu = ["anh","em"]
dong_tu = ["choi","yeu"]
tan_ngu = ["bong da","bong ro"]
for chu in chu_ngu:
    for dong in dong_tu:
        for tan in tan_ngu:
            cau = f"{chu} {dong} {tan}"
            print(cau)
#câu 5
import random 
a = [random,randint(1,99999)for i in range(1000)]
print(a)
#câu 7
List = [["mon",73],["tue",89],["wed",95],["thu",103],["fri",115],["sat",128],["sun",120]]
# cau 3
danh_sach = []
while True:
    phan_tu = int(input("nhap so tu nhien (nhap 0 de ket thuc):"))
    if phan_tu == 0:
        break
    danh_sach.append(phan_tu)
danh_sach_duong = [x for x in danh_sach if x > 0]
danh_sach_am = [x for x in danh_sach if x <= 0]
danh_sach = danh_sach_duong + danh_sach_am
#in danh sach ra man hinh
print("danh sach sau khi chuyen cac phan tu duong lan dau")
print(danh_sach)
# cau 4
numbers = []
while True:
    num = int(input("Nhập một số tự nhiên (nhập 0 để dừng): "))
    if num == 0:
        break
    numbers.append(num)

print("Danh sách gốc:", numbers)

# Chèn [1, 2, 3] vào đầu, cuối và vị trí thứ 5 của danh sách
numbers.insert(0, [1, 2, 3])
numbers.append([1, 2, 3])
numbers.insert(4, [1, 2, 3])

print("Danh sách sau khi chèn [1, 2, 3]:", numbers)

# Xóa phần tử tại vị trí k
k = int(input("Nhập vị trí cần xóa: "))
if k < len(numbers):
    del numbers[k]
else:
    print("Vị trí vượt quá giới hạn của danh sách")

print("Danh sách sau khi xóa phần tử tại vị trí", k, ":", numbers)

# Sắp xếp danh sách theo thứ tự tăng dần và giảm dần
numbers.sort()
print("Danh sách sau khi sắp xếp tăng dần:", numbers)

numbers.sort(reverse=True)
print("Danh sách sau khi sắp xếp giảm dần:", numbers)
#bai 8
n = int(input("Nhập số nguyên dương n: "))

fibonacci = [str(fib) for fib in [0, 1] + [0] * (n - 1)]
for i in range(2, n + 1):
    fibonacci[i] = str(int(fibonacci[i - 1]) + int(fibonacci[i - 2])

print(",".join(fibonacci))
#bai 16
x = int(input("ngao vao gia tri x"))
y = int(input("nhap vao gia tri y"))
list = []
for i in range(0,x):
    list = [i*j for  j in range(o,y)]
    list.append(list)
print(list)
#cau 15 
tuple = []
ten = input("nhap vao ten nguoi dung")
tuoi = ("nhap vao tuoi nguoi dung")
diem = ("nhap diem")
tuple.aooebd(ten,tuoi,diem)
tuple.sort(key=lambda x:(x[0],x[1],x[2]))
print(tuple)
#bai 11
while True:
n = int(input("nhap vao so nguyen"))