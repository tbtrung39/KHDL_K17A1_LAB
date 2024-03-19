n = int(input("Nhập vào ngày trong tuần: "))
if n <= 7 and n >= 1:
    if n == 1:
        print("Sunday")
    elif n == 2:
        print("Monday")
    elif n == 3:
        print("Tuesday")
    elif n == 4:
        print("Wednesday")
    elif n == 5:
        print("Thursday")
    elif n == 6:
        print("Friday")
    elif n == 7:
        print("Saturday")
else: 
    print("Không tồn tại ngày này ")