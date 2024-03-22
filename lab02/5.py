thang = int(input("Nhập vào số tháng trong năm (1-12): "))
if 1 <= thang <= 12:
    if thang == 1:
        print("January")
    elif thang == 2:
        print("February")
    elif thang == 3:
        print("March")
    elif thang == 4:
        print("April")
    elif thang == 5:
        print("May")
    elif thang == 6:
        print("June")
    elif thang == 7:
        print("July")
    elif thang == 8:
        print("August")
    elif thang == 9:
        print("September")
    elif thang == 10:
        print("October")
    elif thang == 11:
        print("November")
    else:
        print("December")
else:
    print("Số tháng không hợp lệ.")