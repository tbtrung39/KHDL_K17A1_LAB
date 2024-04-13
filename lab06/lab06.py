#1
a = [2,-4,1,9,-3,6,3,-2,6,8]

tong_cac_ptu_trong_ds = sum(a)
print("Tong cac phan tu trong danh sach la:",tong_cac_ptu_trong_ds)

dem = 0
S = 0
for i in a:
    if i > 0:
        dem += 1
        S += i
print("Tong cac phan tu cua cac so hang duong la:",S)
print("So luong cac phan tu lon hon 0 la:",dem)

vtri_am_dau_tien = None
for j in range(len(a)):
    if a[j] < 0:
        vtri_am_dau_tien = j
        break
print("So am o vi tri dau tien la:",vtri_am_dau_tien)

vtri_duong_cuoi_cung = None
for k in range(len(a) -1,-1,-1):
    if a[k] > 0:
        vtri_duong_cuoi_cung = k
        break
print("So duong o vi tri cuoi cung la:",vtri_duong_cuoi_cung)

ptu_lon_nhat = max(a)
print("Phan tu lon nhat cua danh sach la:",ptu_lon_nhat)
vtri_lon_nhat_cuoi_cung = len(a) -1 -a[::-1].index(ptu_lon_nhat)
print("Phan tu lon nhat cua danh sach la:",ptu_lon_nhat)
print("Vi tri cua phan tu lon nhat cuoi cung la:",vtri_lon_nhat_cuoi_cung)
#2
n = int(input("Nhap so phan tu danh sach la:"))
danh_sach = []
for i in range(n):
    phan_tu = int(input(f"Nhap phan tu thu {i+1}:"))
    danh_sach.append(phan_tu)
print(danh_sach)

ds_moi = sorted(danh_sach,reverse=True)
b = ds_moi[1]
print(f"Phan tu lon thu 2 la {ds_moi[1]}")
print(f"Vi tri cua phan tu lon thu 2 la: {danh_sach.index(b)}")

dem = 0
max_dem = 0
tong = 0
max_tong = 0
for i in danh_sach:
    if i > 0:
        dem += 1
        tong += i
        max_dem = max(max_dem,dem)
        max_tong = max(max_tong,tong)
    else:
        dem = 0
        tong = 0
print("So luong cac so duong nhieu nhat la:",max_dem)
print("Tong cac so duong lien tiep la:",max_tong)
#3
danh_sach = []
while True:
    n = int(input("Nhap mot so tu nhien (0 de ket thuc nhap) la:"))
    if n == 0:
        break
    danh_sach.append(n)
print(danh_sach)

a = sorted(danh_sach,reverse=True)
print("Danh sach sau khi chuyen so duong len dau la:",a)
m = int(input("Nhap m la:"))
danh_sach.append(m)
danh_sach.insert(0,m)
danh_sach.insert(4,m)
print("Danh sach sau khi chen so m la:",danh_sach)
#4
danh_sach = []
while True:
    n = int(input("nhập vào chuỗi một số nhập ở để kết thúc: ")) 
    if n == 0:
        break
    danh_sach.append(n)
print(f"danh sách sau khi kết thúc chương trình {danh_sach}")
m = [1,2,3]
danh_sach.append(m)
danh_sach.insert(0,m)
danh_sach.insert(4,m)
print(f"danh sách mới sau khi thêm {danh_sach}")
k = int(input("nhập vào vị trí của phần tử thứ k cần xóa: "))
danh_sach.remove(k)
print(f"danh sách sau khi xóa phần tử {k} là {danh_sach}")
danh_sach_moi = [i for i in danh_sach if i != [1,2,3]]
print(f"danh sách sắp xếp theo thứ tự tăng dần là {sorted(danh_sach_moi)}")
print(f"danh sách sắp xếp theo thứ tự giảm dần là {sorted(danh_sach_moi,reverse=True)}")
#5
import random
A = []
for i in range(100000):
    so_ngau_nhien = random.randint(1,99999)
    A.append(so_ngau_nhien)
print("Danh sach 1000 so tu nhien nhau nhien la:",A)
#6
import random
tong = 0
a = []
while True:
    i = random.randint(0,100000)
    tong += i
    a.append(i)
    if len(a) >= 1000:
        break
print("Danh sach 1000 so ngau nhien la:",a)
print(f"Sap xep theo thu tu tang dan {sorted(a,reverse=True)}")
a.sort()
print(f"Sap xep theo thu tu tang dan {a}")
#7
import random
List_ = [["mon",73],["tue",89],["wed",95],["thu",103],["fri",115],["sat",128],["sun",120]]
print("Danh sách list là:",List_)
sublist = List_[2]
print("Độ dài của List_ trước khi thêm:", len(List_))
random_sublist = ["random", random.randint(50, 150)]
List_.append(random_sublist)
print("Độ dài của List_ sau khi thêm:", len(List_))
sum = 0
for day in List_:
    if day[0] in ["tue", "wed", "sat", "sun"]:
        sum += day[1]

print("Tổng sale value trong các ngày thứ 2, thứ 3, thứ 7 và chủ nhật là:", sum)
#8
n = int(input("Nhập số lượng phần tử của dãy Fibonacci: "))
fib_dtien = [0, 1]
for i in range(2, n):
    fib_dtien.append(fib_dtien[-1] + fib_dtien[-2])
fib_tuple = tuple(fib_dtien)
print(",".join(map(str, fib_tuple)))
#10
import random
random_numbers = [x for x in range(201) if x % 35 == 0]
if random_numbers:
    number = random.choice(random_numbers)
    print("Số ngẫu nhiên chia hết cho cả 5 và 7 là:",number)
else:
    print("Không có số nào chia hết cho cả 5 và 7 trong khoảng từ 0 đến 200.")
#11
A = []
B = []
C = []
D = []
while True:
    n = int(input("Nhập số nguyên (0 để kết thúc) là: "))
    if n == 0:
        break
    A.append(n)
print("Danh sách A vừa nhập vào là:", A)
for i in A:
    C.append(i**2)
    if i % 3 == 0 and i % 5 != 0:
        B.append(i)
    if i % 3 ==0:
        D.append(i)
print("Các số trong danh sách A chia hết cho 3 nhưng không chia hết cho 5 là:", B)
print("Danh sách C với các phần tử bình phương của danh sách A là:",C)
print("Danh sách D gồm các phần tử lấy từ danh sách A chia hết cho 3 là:",D)
nhat_ky_giao_dich = []
tien = 0
while True:
    giao_dich = input("Nhập giao dịch (D/W/X để kết thúc): ").strip().upper()
    if giao_dich == 'X':
        break
    for i in giao_dich:
        if i == 'D':
            tien += 100
        if i == 'W':
            tien -= 200
print("Số tiền thực của tài khoản:", tien)
#12
nhat_ky_giao_dich = []
tien = 0
while True:
    giao_dich = input("Nhập giao dịch (D/W/X để kết thúc): ").strip().upper()
    if giao_dich == 'X':
        break
    for i in giao_dich:
        if i == 'D':
            tien += 100
        if i == 'W':
            tien -= 200
print("Số tiền thực của tài khoản:", tien)
#13
chu_ngu = ["Anh","Em"]
dong_tu = ["Chơi","Yêu"]
tan_ngu = ["Bóng đá","Bóng rổ"]
cau = []
for cngu in chu_ngu:
    for dtu in dong_tu:
        for tngu in tan_ngu:
            cau.append(cngu + " " + dtu + " " + tngu)

# In ra tất cả các câu đã tạo
for caus in cau:
    print(caus)
#14
while True:
    password = input("Nhập mật khẩu mới: ")
    if len(password) < 6 or len(password) > 12:
        print("do dai mat khau phai tu 6-12")
    elif not any(c.islower() for c in password):
        print("mat khau phai co it nhat 1 chu trong (a-z).")
    elif not any(c.isupper() for c in password):
        print("mat khau phai co it nhat 1 chu trong (A-Z).")
    elif not any(c.isdigit() for c in password):
        print("mat khau phai co it nhat 1 chu so trong (0-9).")
    elif not any(c in "$#@ " for c in password):
        print("mat khau phai co it nhat 1 ky tu trong ($#@).")
    else:
        print("mat khau hop le!!!")
        break
#15
tuple = []
n = int(input("Nhập số lượng tuple bạn muốn nhập: "))
for i in range(n):
    name = str(input("Nhập tên người dùng là:"))
    age = int(input("Nhập tuổi của người dùng là:"))
    score = float(input("Nhập điểm của người dùng là:"))
    tuple.append((name, age, score))
sorted_data = sorted(tuple, key=lambda x: (x[0], x[1], x[2]))
print("Danh sách các tuple sau khi được sắp xếp:")
for item in sorted_data:
    print(item)
#16
x = int(input("Nhap vao gtri x la:"))
y = int(input("Nhap vao gtri y la:"))
list_cha =[[i*j for j in range(0,y) for i in range(0,x)]]
print(list_cha)
#17
n = int(input("Nhập vào số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập số nguyên dương.")
else:
    ma_tran = [[1 if j == i else 0 for j in range(n)] for i in range(n)]
    # In ra ma trận đơn vị
    print("Ma trận đơn vị bậc", n, "là:")
    for row in ma_tran:
        print(row)
#18
a = []
m = int(input("Nhập số tự nhiên m:"))
n = int(input("Nhập số tự nhiên n:"))
for i in range(m):
    print("Chuẩn bị nhập ma trận hàng thứ ", i+1, ":")
    b = []
    for j in range(n):
        x = int(input("Nhập phần tử thứ "+ str(j+1) + ":"))
        b = b + [x]
    a.append(b)
print("Ma trận đã nhập xong !")
for i in range(m):
    for j in range(n):
        print(a[i][j], end = " ")
    print()