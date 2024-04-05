#1
str = input("Nhap chuoi ky tu la:")
print("Chuoi ky tu vua nhap la:",str)
dem = 0
for c in str:
    if "0" <= c <= "9":
        dem += 1
print("So ky tu la so trong chuoi vua nhap la:",dem)
#2
str = input("Nhap chuoi ky tu la:")
print("Chuoi ky tu vua nhap la:",str)
dem1 = 0
dem2 = 0
for c in str:
    if c.isalpha():
        dem1 += 1
    if "0" <= c <= "9":
        dem2 += 1
print("So ky tu khong la so trong chuoi str la:",dem1)
print("So ky tu khong la chu cai tieng anh la",dem2)
#3
a = int(input("Nhap so tu nhien la:"))
he_so = ''
if a == 0:
    print("So nhi phan la: 0")
else:
    while a > 0:
        he_so = str(a % 2) + he_so
        a //= 2
print("So nhi phan la:",he_so)
#4
str1 = input("Nhap chuoi str1 la:")
str2 = input("Nhap chuoi str2 la:")
do_dai1 = len(str1)
do_dai2 = len(str2)
tron1 = 0
tron2 = 0
hop = ''
while tron1 < do_dai1 or tron2 < do_dai2:
    if tron1 < do_dai1:
        hop += str1[tron1]
        tron1 += 1
    if tron2 < do_dai2:
        hop += str2[tron2]
        tron2 += 1
print("Sau khi tron sau str1 va str2 la:",hop)
#5
str = input("Nhap chuoi ky tu la:")
chuoi = "".join(char for char in str if char.isdigit())
print(chuoi)
chuoi = int(chuoi)
s = 0
for i in range(1,chuoi):
    if chuoi % i ==0:
        s += 1
        if s == chuoi:
            print(chuoi,"la so hoan hao")
            break
else:
    print(chuoi,"khong la so hoan hao")
#6
import math
str = input("Nhập chuỗi str tu bàn phím là: ")
chuoi_he_hex = '0123456789ABCDEF'
he_hex = ''.join(char for char in str if char in chuoi_he_hex)
chuyen_doi = sum(int(x, 16) * math.pow(16, len(he_hex)-i-1) for i, x in enumerate(he_hex)) 
print("Chuỗi sau khi chuyển đổi là: ", chuyen_doi) 
#7
van_ban = input("Nhap mot doan van ban hoan chinh la:")
tu_don = input("Nhap vao mot tu don la:")
dem = 0
do = 0
while True:
    do = van_ban.find(tu_don,do)
    if do == -1:
        break
    dem += 1
    do += 1
print("So lan tu",tu_don,"xuat hien trong",van_ban,"la:",dem)
#8
str = input("Nhập chuỗi ký tự là: ")
max_chuoi = ""
chuoi_con = str[0]
for i in range(1, len(str)):
    if str[i] == str[i - 1]:
        chuoi_con += str[i]
    else:
        if len(chuoi_con) > len(max_chuoi):
            max_chuoi = chuoi_con
            chuoi_con = str[i]
print(max_chuoi)
#9
str1 = str(input("nhập chuỗi 1: "))
str2 = str(input("Nhập chuỗi 2: "))
a = ''.join(i for i in str1 if i in str2)
print(a)
#10
str = input("nhap chuoi he nhi phan la:")
nhi_phan = True
for c in str:
    if c != '0' and c != '1':
        nhi_phan = False
        break
if nhi_phan:
    doi_he_tp = 0
    for i in range(len(str)):
        doi_he_tp += int(str[i])*(2**(len(str)-i-1)) 
    print("So thap phan tuong ung voi he nhi phan la:",doi_he_tp)
else:
    print("Chuoi nhi phan nhap vao ban phim khong hop le !!!")
#11
str1 = input("Nhap chuoi ky tu la:")
tu = str1.split()
print(tu)
#12
a = input("Nhập chuỗi số a: ")
b = input('Nhập chuỗi số b: ')
for i in range(1 , len(a)):
    for j in range(1, len(b)):
        A = (a[:i])
        B = (a[i:])
        C = (b[:j])
        D = (b[i:])
    if int(A) + int(B) != int(C) + int(D):
        print("Không tồn tại cách đặt")
    else:
        print(f"{A} + {B} = {C} + {D}")