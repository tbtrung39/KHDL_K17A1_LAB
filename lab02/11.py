ngay=int(input("nhập ngày số: "))
thang=int(input("nhập tháng: "))
if thang==1 or thang ==3 or thang==5 or thang==7 or thang==8 or thang==10 or thang==12:
    if ngay>0 and ngay<31:
        ngay_tiep_theo=ngay+1
        print("ngày tiếp theo là: ",ngay_tiep_theo)
    elif ngay==31:
        print("ngày tiếp theo là: 1")
    else:
        print("số ngày không hợp lệ!!!")
elif thang==2:
    if ngay>0 and ngay<28:
        ngay_tiep_theo=ngay+1
        print("ngày tiếp theo là: ",ngay_tiep_theo)
    elif ngay==28:
        print("ngày tiếp theo là: 1")
    else:
        print("số ngày không hợp lệ!!!")
elif thang==4 or thang==6 or thang==9 or thang==11:
    if ngay>0 and ngay<30:
        ngay_tiep_theo=ngay+1
        print("ngày tiếp theo là: ",ngay_tiep_theo)
    elif ngay ==30:
        print("ngày tiếp theo là: 1")
    else:
        print("số ngày không hợp lệ!!!")
else:
    print("số tháng không hợp lệ!!!")