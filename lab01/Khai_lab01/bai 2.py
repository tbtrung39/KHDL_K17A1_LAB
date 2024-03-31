#bài 2
s=float(input('nhập số giây:'))
m=float(input('nhập số phút:'))
h=float(input('nhập số giờ:'))
d=float(input('nhập số ngày:'))
if s>60:
    s1=s%60
    m=m+s//60
if m>60:
    m1=m%60
    h=h+m//60    
if h>24:
    h1=h%24
    d=d+h//24
print(f'{d} ngày {h1} giờ {m1} phút {s1} giây')