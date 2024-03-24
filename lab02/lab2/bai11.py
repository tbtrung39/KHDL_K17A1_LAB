nam = 2024
thang = 2 
ngay = 28
so_ngay_trong_thang = 0
if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
    so_ngay_trong_thang = 31
elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
    so_ngay_trong_thang = 30
else:
    if (nam % 4 == 0 and nam % 100 != 0 ) or (nam % 400 == 0):
        ngay = 29

if ngay < so_ngay_trong_thang:
    ngay += 1
else:
    day = 1
    if thang == 12:
        thang = 1
        nam += 1
    else:
        thang += 1
print("ngay tiep theo la", nam, "thang", thang, "ngay",ngay)