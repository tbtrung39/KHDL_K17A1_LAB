thang=int(input('Nhập tháng bạn cần kiểm tra :'))
if thang==2:
    print(f'Tháng {thang} có 28 or 29 ngày ')
elif thang==4 or thang==6 or thang==9 or thang==11 :
    print(f'Tháng {thang} có 30 ngày ')
elif thang==1 or thang==3 or thang==5 or thang==7 or thang==8 or thang==10 or thang==12:
    print(f'Tháng {thang} có 31 ngày')
else:
    print(f'Tháng {thang} không tồn tại')