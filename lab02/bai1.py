import math
n = int(input("Nhập vào một tháng(1-12): "))
x = 2
if 1<= n <= 12:
    if n % x == 0:
        print("Tháng có 30 ngày")
    elif n == x:
        if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
            print("Tháng có 29 ngày")
        else: 
            print("Tháng có 28 ngày")
    elif n % x != 0:
        print("Tháng có 31 ngày")
else:
    print("Giá trị tháng không hợp lệ. Vui lòng nhập lại từ 1 đến 12")