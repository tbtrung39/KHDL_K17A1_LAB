thu = int(input("Nhập vào số thứ trong tuần (1-7): "))
if 1 <= thu <= 7:
    if thu == 1:
        print("Sunday")
    elif thu == 2:
        print("Monday")
    elif thu == 3:
        print("Tuesday")
    elif thu == 4:
        print("Wednesday")
    elif thu == 5:
        print("Thursday")
    elif thu == 6:
        print("Friday")
    else:
        print("Saturday")
else:
    print("Số thứ không hợp lệ")