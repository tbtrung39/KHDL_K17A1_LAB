day = 28
thang = 2
nam = 2023

if (nam % 4 == 0 and nam % 100 != 0) or nam % 400 == 0:
    ngay_trong_thang = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    ngay_trong_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if day < ngay_trong_thang[thang - 1]:
    ngaytiep = day + 1
    thangtiep = thang
    nam_tiep = nam
else:
    ngaytiep = 1
    if thang < 12:
        thangtiep = thang + 1
        nam_tiep = nam
    else:
        thangtiep = 1
        nam_tiep = nam + 1

print("Ngày tiếp theo là: {}-{}-{}".format(ngaytiep, thangtiep, nam_tiep))