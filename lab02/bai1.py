n = int(input("Nhập vào tháng: "))
if n <= 12 and n >=1:
    if n == 4 or n == 6 or n == 9 or n == 11:
        print("30 ngày ")
    elif n == 2:
        print(" 28 hoặc 29 ngày")
    else:
        print("31 ngày")
else:
    print("không tồn tại tháng")