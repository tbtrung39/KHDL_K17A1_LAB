thang=int(input("nhập một tháng bất kỳ: "))
nam=int(input("nhập năm cần kiêm tra: "))
if thang ==1 or thang==3 or thang==5 or thang==7 or thang ==8 or thang==10 or thang==12:
    print("tháng", thang, "có 31 ngày")
elif thang ==4 or thang ==6 or thang==9 or thang :
    print("tháng", thang, "có 30 ngày")
elif thang ==2:
    if (nam%4==0 and nam%100 !=0) or (nam%400 ==0):
        print('tháng', thang, "có 29 ngày")
    else:
        print('tháng', thang, "có 28 ngày")