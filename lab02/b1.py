month=int(input("nhap vao mot thang: "))
if month >12 or month <1:
    print("vui long nhap lai mot thang ")
else:
    if month == 1 or month == 3 or month ==5 or month ==7 or month ==8 or month ==10 or month == 12:
        print("thang {} co 31 ngay".format(month))
    elif month == 4 or month == 6 or month == 9:
        print("thang {} co 30 ngay".format(month))
    elif month ==2 :
        print("thang 2 co 28 hoac 29 ngay")