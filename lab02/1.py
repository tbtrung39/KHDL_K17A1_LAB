thang=int(input("Nhap ten thang:"))
if thang ==1 or thang==3 or thang==5 or thang==7 or thang==8 or thang==10 or thang==12:
    print("Thang",thang ,"co 31 ngay")
elif thang==2:
    print("Thang 2 co 28 ngay hoac 29 ngay")
elif thang==4 or thang==6 or thang==9 or thang==11:
    print("thang",thang,"co 30 ngay")
else:
    print("nhap lai thang hop le")