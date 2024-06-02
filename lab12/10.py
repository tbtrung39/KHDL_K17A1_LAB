while True:
    try:
        ngay = int(input("ngay: "))
        thang = int(input("thang: "))
        nam = int(input("nam: "))
        ngay2 = int(input("ngay2: "))
        thang2 = int(input("thang2: "))
        nam2 = int(input("nam2: "))

        if ngay < 0 or thang < 0 or thang > 12 or nam < 0 or ngay2 < 0 or thang2 < 0 or thang2 > 12 or nam2 < 0:
            raise ValueError
        if thang and thang2 in [1, 3, 5, 7, 8, 10, 12]:
            if ngay > 31 or ngay2 > 31 or ngay < 0:
                raise ValueError
        elif thang and thang2 in [4, 6, 9, 11]:
            if ngay > 30 or ngay2 > 30 or ngay < 0:
                raise ValueError
        elif thang and thang2 == 2:
            if (nam and nam2 % 4 == 0 and nam and nam2 % 100 != 0) or (nam and nam2 % 400 == 0):
                if ngay > 29 or ngay2 > 29 or ngay < 0:
                    raise ValueError
            else:
                if ngay > 28 or ngay2 > 28 or ngay < 0:
                    raise ValueError
        break
    except ValueError:
        print("sai")

nam_moi = nam2 - nam
thang_moi = thang2 - thang
ngay_moi = ngay2 - ngay
if ngay_moi < 0:
    thang_moi = thang_moi - 1
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        ngay_moi = ngay_moi + 31
    elif thang in [4, 6, 9, 11]:
        ngay_moi = ngay_moi + 30
    elif thang == 2:
        if (nam_moi % 4 == 0 and nam_moi % 100 != 0) or (nam_moi % 400 == 0):
            ngay_moi = ngay_moi + 29
        else:
            ngay_moi = ngay_moi + 28
print("cách nhau: ", ngay_moi, thang_moi, nam_moi)