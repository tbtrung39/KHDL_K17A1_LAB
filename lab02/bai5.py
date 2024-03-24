n = int(input("Nhập số tháng: "))
if n<1 and n>12:
    print("Tháng nhập vào không hợp lệ")
else:
    if n == 1:
        print("January")
    elif n == 2:
        print("February")
    elif n == 3: 
        print("March")
    elif n == 4: 
        print("April")
    elif n == 5: 
        print("May")
    elif n == 6: 
        print("June")
    elif n == 7: 
        print("July")
    elif n == 8: 
        print("August")
    elif n == 9: 
        print("September")
    elif n == 10: 
        print("October")
    elif n == 11: 
        print("November")
    else: 
        print("December")