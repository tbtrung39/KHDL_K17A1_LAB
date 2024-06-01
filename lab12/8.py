ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

if ngay > 1:
    ngay_truoc = ngay - 1
    thang_truoc = thang
    nam_truoc = nam
else:
    if thang > 1:
        if thang in [2, 4, 6, 8, 9, 11]:
            ngay_truoc = 31
            thang_truoc = thang - 1
        elif thang == 3:
            if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
                ngay_truoc = 29
            else:
                ngay_truoc = 28
            thang_truoc = thang - 1
        else:
            ngay_truoc = 30
            thang_truoc = thang - 1
        nam_truoc = nam
    else:
        ngay_truoc = 31
        thang_truoc = 12
        nam_truoc = nam - 1

print("Ngày trước đó là: {}/{}/{}".format(ngay_truoc, thang_truoc, nam_truoc))
