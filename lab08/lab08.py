#1
def bai1(x):
    return x + 1
x = int(input("x:"))
y = bai1(x)
print(y)
#2
def ucln(x,y):
    while y!= 0:
        x,y = x , x % y
        return x

def rutgon(a, b):
    Ucln = ucln(a, b)
    rg_a = a / Ucln
    rg_b = b / Ucln
    return rg_a, rg_b

tu_so = int(input("Nhập tử số: "))
mau_so = int(input("Nhập mẫu số: "))

tu_rut_gon, mau_rut_gon = rutgon(tu_so, mau_so)

print( tu_rut_gon, "/", mau_rut_gon) 
#3
def kiem_tra_so_nguyen_to(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def in_so_nguyen_to(n):
    so_nguyen_to = []
    for num in range(2, n):
        if kiem_tra_so_nguyen_to(num):
            so_nguyen_to.append(num)
    return so_nguyen_to

n = int(input("Nhập một số nguyên dương n: "))
so = in_so_nguyen_to(n)
print(so)
#4
def tinh_lap_phuong(so_nguyen):
    lap_phuong = so_nguyen ** 3
    return lap_phuong

so_nguyen = int(input("Nhập một số nguyên: "))
lap_phuong = tinh_lap_phuong(so_nguyen)
print( lap_phuong)
#5
def ucln(x,y):
    while y!= 0:
        x,y = x , x % y
        return x

x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
uoc_chung = ucln(x,y)
print(uoc_chung)
#6
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def bcnn(a, b):
    ucln = ucln(a, b)
    return (a * b) // ucln
so_a = int(input("Nhập a: "))
so_b = int(input("Nhập b: "))
Bcnn = bcnn(so_a, so_b)
print( Bcnn)
#7
def gtln(a,b,c):
    ln = max(a,b,c)
    nn = min(a,b,c)
    return ln , nn 
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
gt = gtln(a,b,c)
print(gt)
#8
def chu_vi(r):
    C = 2 * 3.14 * r
    return C
def dien_tich(r):
    S = 3.14 * r ** 2
    return S
r = int(input("r: "))
C = chu_vi(r)
S = dien_tich(r)

print("Chu vi của hình tròn là:", C)
print("Diện tích của hình tròn là:", S)
#9
def coban(a,b):
    cong = a + b
    tru = a -b
    nhan = a * b
    chia = a / b
    return cong, tru , nhan , chia

a = int(input("A: "))
b = int(input("B;"))
COban = coban(a,b)    
print("Cộng Trừ Nhân Chia lần lượt: ",COban)
#10
def uoc_so(n):
    uoc = []
    for i in range(1, n + 1):
        if n % i == 0:
            uoc.append(i)
    return uoc

n = int(input("n: "))
cac_uoc_so = uoc_so(n)
print("ước số", cac_uoc_so)
#11
def input():
    ho_ten = input("Tên: ")
    diem_toan = float(input("Điểm Toán: "))
    diem_ly = float(input("Điểm Lý: "))
    diem_hoa = float(input("Điểm Hóa: "))
    return ho_ten, diem_toan, diem_ly, diem_hoa

def trung_binh(diem_toan, diem_ly, diem_hoa):
    diem_trung_binh = (diem_toan + diem_ly + diem_hoa) / 3
    return diem_trung_binh

def xuat(ho_ten, diem_trung_binh):
    print("Họ tên sinh viên:", ho_ten)
    print("Điểm trung bình:", diem_trung_binh)

ho_ten, diem_toan, diem_ly, diem_hoa = input()
diem_tb = trung_binh(diem_toan, diem_ly, diem_hoa)
xuat(ho_ten, diem_tb)
#12
def  nv ():
    n  =  input ( "Nhập vào mười nhân viên: " )
    qq  =  input ( "Nhap vao que quan cua nhan vien: " )
    tn  =  int ( input ( f"Nhap vao tham nien cua nhan vien tinh theo nam: " ))
    luong  =  6000000  *  tn  * ( 5 / 100 )
    return  n , qq , tn , luong
x  =  int ( input ( "Nhap vao so luong nhan vien can nhap thong tin: " ))
lst  = []
for  i  in  range( x ):
    lst . append( nv ())
print ( f"Danh sách thông tin có bản cua { x } nhân viên nhap tu ban phím lan luot tu ten, que quan, tham nien và luong { lst } " )
#13
def ktra_nam(y):
    if y % 4 == 0 and ( y % 100 != 0 or y % 400 != 0):
        return True
    else:
        return False

def thang(t, y):
    if t <= 12 and t >= 1:
        if t == 4 or t == 6 or t == 9 or t == 11:
            return "30 ngày"
        elif t == 2:
            if ktra_nam(y):
                return "29 ngày"
            else:
                return "28 ngày"
        else:
            print("31 ngày")

y = int(input("Năm: "))
year = ktra_nam(y)
print(year)


t = int(input("Tháng: "))
Thang = thang(t,y)
print(Thang)
#14
def lst_int(n):
    lst = []
    for a in range(n):
        a = int(input(f" số nguyên thứ {a +1 } : "))
        lst.append(a)
    return lst
n = int(input("số lương: "))
lstbp = lst_int()
binh = list(map(lambda a : a**2, lstbp))
print(f"danh sách các số nguyên a sau khi bình phương là {binh}")
#15
def lst_int(n):
    lst = []
    for a in range(n):
        a = int(input(f" số nguyên thứ {a +1 } : "))
        lst.append(a)
    return lst
n = int(input("số lương: "))
lstlbp = lst_int()
even_n = [i for i in lstlbp if i % 2 != 0]
binh = list(map(lambda a: a**2, even_n))
print(f"danh sách các số nguyên a lẻ sau khi bình phương là {binh}")
#16
def bai16():
    lst = []
    for i in range(1,101):
        if i % 2 == 0:
            lst.append(i)
    return lst

print(bai16())
#17
from functools import reduce
def sum_int(n):
    lst = []
    for a in range(n):
        a = int(input(f" số nguyên thứ {a +1 } : "))
        lst.append(a)
    return lst
n = int(input("Nhập n: "))
lstcbp = sum_int(n)
even_n = list(filter(lambda x: x % 2 == 0, lstcbp))
sum_n = reduce(lambda x, y: x + y, even_n)
print("Tổng các số chẵn từ 1 đến n là:", sum_n)

