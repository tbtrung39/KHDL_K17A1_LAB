thang=int(input('Nhap vao mot thang cần kiểm tra :'))
if thang >0 and thang <=12:
    if thang<8 and thang %2 !=0:
        print(f'Tháng {thang} có 31 ngày')
    elif 8<=thang and thang%2==0:
        print(f'Tháng {thang} có 31 ngày')
    elif 2<thang<8 and thang%2==0:
        print(f'Tháng {thang} có 30 ngày')
    elif thang>8 and thang %2!=0:
        print(f'Tháng {thang} có 30 ngày')
    elif thang==2:
        nam=int(input('Nhập năm cần kiểm tra: '))
        if nam % 4 == 0 and nam % 100 != 0 or nam % 400 == 0:
            print(f'Tháng 2 năm {nam} là năm nhuận nên có 29 ngày.')
        else:
            print(f'Tháng 2 năm {nam} không là năm nhuận nên có 28 ngày.')
else:
    print("Không có tháng này!!!")