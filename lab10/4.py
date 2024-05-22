from packages import giaiphuongtrinh as md
t = int(input('Chon phuong trinh muon giai: (1 or 2): '))
if t == 1:
    print('ax+b=0')
    a = float(input('Nhap a: '))
    b = float(input('Nhap b: '))
    print(md.phuong_trinh_bac1(a,b))
if t == 2:
    print('ax^+bx+c=0')
    a = float(input('Nhap a: '))
    b = float(input('Nhap b: '))
    c = float(input('Nhap c: '))
    print(md.phuong_trinh_bac2(a,b,c))
    