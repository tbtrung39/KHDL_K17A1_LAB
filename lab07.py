#1
a = set()
while True:
    n=input("Nhap ki tu(nham phim Esc de ket thuc):")
    if n =="esc":
        break
    a.add(n)
a -= {n for n in a if n.isdigit()}
print("Tap hop la:",a)
#2
number=[]
while True:
    n = input("nhap gia tri:")
    if n =="esc":
        break
    number.append(n)
    a = set(number)
    print(a)
#3
import random
n = int(input("nhap so luong phan tu cua tap hop A:"))
A = [random.uniform(-100, 100) for _ in range(n)]
min = 0
max = 0
for x in A:
    if x < min:
        min = x
    if x > max:
        max = x
tong = 0
for x in A:
    tong =+ x
print("tap hop A:", A)
print("phan tu nho nhat:", min)
print("phan tu lon nhat:", max)
print("tong cac phan tu:", tong)
#4
chieu_cao = [1161,182,161,154,176,170,167,171,170,174,150,142,148,165,170,178,156,145,149,163,162,159,165,165,170.180,155,159,155,153,152,162,180,168,169,167,170]
#nhom co bao nhieu sinh vien
so_luong_sv = len(chieu_cao)
print("So luong sinh vien trong nhom la:", so_luong_sv)
#chieu cao trung binh cua cac sinh vien
trung_binh = sum(chieu_cao)/so_luong_sv
print("chieu cao trung binh cua sinh vien trong nhom la:",round(trung_binh,2))
#5
import random
digits = [0,1,2,3,4,5,6,7,8,9]
A = random.sample(digits, 5)
print(A)
#6
n = int(input("Nhap so tu nhien :"))
so_nguyen_to=set()
dem=0
so=2
while dem < n:
    la_so_nguyen_to = True
    for i in range(2, int(so**0.5)+1):
        if so % i ==0:
            la_so_nguyen_to=False
            break
    if la_so_nguyen_to:
        so_nguyen_to.add(so)
        dem+=1
    so +=1
print(f"{n} so nguyen to dau tien la:",so_nguyen_to)
#7
A = set(input("Nhập tập hợp A (các ký tự chữ và số, cách nhau bằng dấu cách): ").split())
B = set(input("Nhập tập hợp B (các ký tự chữ và số, cách nhau bằng dấu cách): ").split())
pt_chung = A.intersection(B)
print("Các phần tử chung của tập hợp A và tập hợp B là:", pt_chung)
#8
import random
A = set()
for _ in range(10):
    element_type = random.choice(['int', 'float', 'str'])
    if element_type == 'int':
        A.add(random.randint(1, 100))  
    elif element_type == 'float':
        A.add(random.uniform(1.0, 100.0))  #
    else:
       A.add("".join(random.choice("abcdefghijklmnopqrstuvwxyz")))
dem_int = 0
dem_float = 0
dem_str = 0
for element in A:
  if isinstance(element, int):
    dem_int += 1
  elif isinstance(element, float):
    dem_float += 1
  else:
    dem_str += 1

print("Số phần tử là số nguyên:", dem_int)
print("Số phần tử là số thực:", dem_float)
print("Số phần tử là chuỗi ký tự:", dem_str)
#9
n = int(input("nhap so tu nhien n:"))
a=set()
for i in range(1,n):
    if n%i==0:
        a.add(i)
    else:
        so_nguyen_to=set()
        for j in range(2,n):
            la_so_nguyen_to = True
            for k in range(2, int(j**0.5)+1):
                if j%k==0:
                    la_so_nguyen_to=False
                    break
            if la_so_nguyen_to:
                so_nguyen_to.add(j)
b=so_nguyen_to-a
print("A:",a)
print("B:",b)
#10
m = eval(input("Nhập số tự nhiên: "))
n = eval(input("Nhập số tự nhiên: "))
m = set(m) ; n = set(n)
f = m.intersection(n)
print("Các chữ số chung: ",f)
tong = 0
for i in f:
    tong += i
print("Tổng các chữ số chung của m và n: ",tong)
#11
c={1,2,3,4,5,6,7,8,9,10,11}
j={1,3,6,7,8}
p={1,4,3,9,10,11}
all = c & j & p
print(all )
a=(c.intersection(j).difference(p))|(c.intersection(p).difference(j))|(j.intersection(p).difference(c))
print(a)
b=(c.symmetric_difference(j).symmetric_difference(p)) - all 
print(b)
#12
dict_n = {}
n = int(input("Nhập số nguyên: "))
for i in range(1,n+1):
    dict_n[i] = i*i
print("Kết quả: ",dict_n)
#13
a=dict()
for i in range(1,101):
    j=i
    thap_phan=""
    while j >0:
        so_du=j%2
        thap_phan=str(so_du) + thap_phan
        j = j //2
        a.update({i : thap_phan})
print(a)
#14
dct_nhi_phan={}
n=int(input("nhap so n: "))
for i in range(1,n):
    chuoi_nhi_phan=''
    num=i
    while num>0:
        chuoi_nhi_phan=str(num%2)+chuoi_nhi_phan
        num//=2
        dct_nhi_phan[i]=chuoi_nhi_phan
print(dct_nhi_phan)
#15
a = [2, 3, 4, 5, 6, 7, 8, 9]
b = ["T", "Q", "Y", "H", "N", "B", "P", "G"]
dic = {}
for i in range(len(a)):
    dic[a[i]] = b[i]
print(dic)
#16
a=[1,20,31,4,5]
dict={}
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[j] +1==a[j]:
            dict[i]=j
print(dict)
#17
n = int(input("số lượng: "))
thong_tin_sv = {}
for i in range(n):
    ma_sv = input("mã sinh viên: ")
    ten_sv = input(" tên : ")
    diem_sv = float(input(" điểm: "))
    lam_tron_diem = max(0, min(10, round(diem_sv))) 
    thong_tin_sv[ma_sv] = {"name": ten_sv, "score": lam_tron_diem}
diem_giam_dan = sorted(thong_tin_sv.items(), key=lambda x: x[1]["score"], reverse=True)
print("Danh sách sinh viên theo điểm giảm dần:")
for ma_sv, info in diem_giam_dan:
    print("Mã sinh viên:", ma_sv)
    print("Tên sinh viên:", info["name"])
    print("Điểm số:", info["score"])
    print()
#18
tcdt = {}
n = int(input("nhập vào số lượng thí sinh: "))
for i in range(n):
    sbd = int(input(f"nhập vào số báo danh của thí sinh số {i + 1}: "))
    name = str(input(f"nhập vào tên của thí sinh số {i + 1}: "))
    score = float(input(f"nhập vào điểm thi của thí sinh số {i + 1}: "))
    tcdt[sbd] = {"name":name,"score":score}
a = int(input("nhập vào sbd của thí sinh cần kiểm tra: "))
if a in tcdt:
    ts = tcdt[a]
    print(f"số báo danh của thí sinh đó là {a}")
    print(f"họ và tên của thí sinh đó {ts['name']}")
    print(f"điểm của thí sinh đó {ts['score']}")
else:
    new_name = str(input("nhập vào tên của thí sinh mới}: "))
    new_score =  float(input("nhập vào điểm thi của thí sinh mới: "))
    tcdt[a] = {"name":new_name,"score":new_score}
print(tcdt)
