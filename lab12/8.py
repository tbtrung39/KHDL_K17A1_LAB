while True:
    try:
        ngay = int(input("ngay: "))
        thang = int(input("thang: "))
        nam = int(input("nam: "))
        if ngay < 0 or ngay > 31 or thang > 12 or nam < 0:
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

thang_31_ngay = [1, 3, 5, 7, 8, 10, 12]
thang_30_ngay = [4, 6, 9, 11]
nam_nhuan = (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)

if thang in thang_31_ngay:
    max = 31
elif thang in thang_30_ngay:
    max = 30
else:
    if thang == 2 and nam_nhuan:
        max = 29
    else:
        max = 28

if ngay >= 28:
    ngay = 1
    if thang == 12:
        thang = 1
        nam = nam + 1
    else:
        thang = thang + 1
else:
    ngay = ngay + 1

print("ngay tiep: ", ngay, thang, nam)
