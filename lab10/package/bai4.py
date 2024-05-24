from __pycache__ import gpt 
n = int(input('Chon phuong trinh muon giai: (1 or 2): '))
if n == 1:
    print('ax+b=0')
    a = float(input('Nhap a: '))
    b = float(input('Nhap b: '))
    print(gpt.phuong_trinh_bac1(a,b))
if n == 2:
    print('ax^+bx+c=0')
    a = float(input('Nhap a: '))
    b = float(input('Nhap b: '))
    c = float(input('Nhap c: '))
    print(gpt.phuong_trinh_bac2(a,b,c))
