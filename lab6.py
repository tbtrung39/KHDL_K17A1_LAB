#1
#diem so luong cac so hang duong va tong cua cac so hang duong
so_hang_duong=0
a=[2,-4,1,9,-3,6,3,0,-2,6,8]
tong_duong=0
for i in a:
    if i>0:
        so_hang_duong+=1
        tong_duong+=i
print("so luong cac so hang duong",so_hang_duong)
print("tong cac so hang duong",tong_duong)
#tim vi tri cau phan tu am dau tien cua danh sach
i=0
while i <len(a):
    if a[i]<0:
        vi_tri_am=i
        break
    i+=1
print("vi tri phan tu am dau tien la ",vi_tri_am)
#tim phan tu duong cuoi cung trong danh sach
for i in range(len(a)-1,-1,-1):
    if a[i]>0:
        vi_tri_duong=i
        break
#tim vi tri lon nhat trong danh sachva vi tri lon nhat cuoi cung
a.reverse
print(a)
max=0
vi_tri=0
for i in range(0,len(a)):
    if a[i]>max:
        max=a[i]
        vi_tri=i
print(f"phan tu lon nhat trong danh sach la:{max},va vi tri cua phan tu lon nhat la:{vi_tri}")
#2
import random
n=int(input("nhap gia tri n: "))
list=[]
for i in range(n):
    j=random.randint(-100,100)
    list.append(j)
print(list)
a=sorted(list)
a.remove()
print(a[1])
tong=0
for k in a:
    if k>0:
        tong+=k
print(tong)
#3
list=[]
while True:
    n=int(input("Nhập số tự nhiên:"))
    if n ==0:
        break
    list.append(n)
print(list)
so_duong=[i for i in list if i>0]
so_am=[j for j in list if j<0]
list=so_duong + so_am
print("danh sach khi thay doi: ",list)
m=int(input("nhập giá tri m:"))
list.insert(0,m)
list.append(m)
list.insert(4,m)
print("Danh sach moi",list)
#4
danh_sach=[]
while True:
   n=int(input("nhap so tu nhien :"))
   if n<=0:
      break
   danh_sach.append(n)
   print("Danh sach sau khi nhap:",danh_sach)
#chen phan tu vao danh sach
danh_sach.append([1,2,3])
print("danh sach sau khi chen them phan tu:",danh_sach)
danh_sach.insert(0,[1,2,3])
print(danh_sach)
danh_sach.append(4,[1,2,3])   
print(danh_sach) 
#xoa phan tu khoi danh sach
k=int(input("nhap vi tri phan tu can xoa"))  
danh_sach.pop(k)
print("danh sach sau khi xoa:",danh_sach)
#5
import random
A = []
for a in range(1000):
    so = random.randint(0,100000)
    A.append(so)
print("Danh sách A gồm 1000 số tự nhiên:")
print(A)
#6
import random
#cach 1
lst=[random.randint(1,99999) for i in range(1000)]
ds_sap_xep=sorted(lst)
print("danh sach da sap xep la:", ds_sap_xep)

#cach 2
lst=[random.randint(1,99999) for i in range(1000)]
for i in range(len(lst)):
    for j in range(len(lst)-1):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
print("danh sach da sap xep la:", lst)
#7
list_ = [
    ["mon", 73],
    ["tue", 89],
    ["wed", 95],
    ["thu", 103],
    ["fri", 115],
    ["sat", 128],
    ["sun", 120],
]
# In các phần tử ra màn hình.
for i in list_:
    print(i, end=",")
print("\n")
# Chọn ra phàn tử thứ hai, thuộc vi trí thứ ba.
print(list_[2])
#8
n = int(input("Nhập n: "))
lst = [i0 := 0, i1 := 1] + [i1 := i0 + (i0 := i1) for _ in range(2, n + 1)]
print(lst)
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