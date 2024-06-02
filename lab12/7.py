while True:
    try:
        ngay = int(input("ngay: "))
        thang = int(input("thang: "))
        nam = int(input("nam: "))
        if ngay < 0 or ngay > 31 or thang < 0 or thang > 12 or nam < 0:
            raise ValueError
        if thang in [1, 3, 5, 7, 8, 10, 12]:
            if ngay > 31 or ngay < 0:
                raise ValueError
        elif thang in [4, 6, 9, 11]:
            if ngay > 30:
                raise ValueError
        elif thang == 2:
            if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
                if ngay > 29:
                    raise ValueError
            else:
                if ngay > 28:
                    raise ValueError
        break
    except ValueError:
        print("sai")

if ngay != 1:
    ngay = ngay - 1
else:
    if thang == 1:
        ngay = 31
        thang = 12
        nam = nam - 1
    elif thang in [1, 3, 5, 7, 8, 10, 12]:
        ngay = 31
        thang = thang - 1
    elif thang in [4, 6, 9, 11]:
        ngay = 30
        thang = thang - 1
    else:
        thang = thang - 1
        if thang == 2:
            if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
                ngay = 29
            else:
                ngay = 28
print("ngay truoc: ", ngay, thang, nam)