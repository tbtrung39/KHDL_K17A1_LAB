num = int(input("Nhập số nguyên có ba chữ số: "))
a = num // 100
b = (num % 100) // 10
c = num % 10
if a == 1:
    print("Một trăm", end=' ')
elif a == 2:
    print("Hai trăm", end=' ')
elif a == 3:
    print("Ba trăm", end=' ')
elif a == 4:
    print("Bốn trăm", end=' ')
elif a == 5:
    print("Năm trăm", end=' ')
elif a == 6:
    print("Sáu trăm", end=' ')
elif a == 7:
    print("Bảy trăm", end=' ')
elif a == 8:
    print("Tám trăm", end=' ')
elif a == 9:
    print("Chín trăm", end=' ')
if b != 0:
    if b == 1:
        print("mười", end=' ')
    elif b == 2:
        print("hai mươi", end=' ')
    elif b == 3:
        print("ba mươi", end=' ')
    elif b == 4:
        print("bốn mươi", end=' ')
    elif b == 5:
        print("năm mươi", end=' ')
    elif b == 6:
        print("sáu mươi", end=' ')
    elif b == 7:
        print("bảy mươi", end=' ')
    elif b == 8:
        print("tám mươi", end=' ')
    elif b == 9:
        print("chín mươi", end=' ')
if c != 0 and b != 1:
    if c == 1:
        print("một")
    elif c == 2:
        print("hai")
    elif c == 3:
        print("ba")
    elif c == 4:
        print("bốn")
    elif c == 5:
        print("lăm")
    elif c == 6:
        print("sáu")
    elif c == 7:
        print("bảy")
    elif c == 8:
        print("tám")
    elif c == 9:
        print("chín")