str = "Khoa, khoa học ứng dụng* gồm các từ: 'Khoa', 'khoa', 'học', 'ứng' 'dụng'."
tu = ""  
for ky_tu in str:
    if ky_tu != " " and ky_tu != "," and ky_tu != "'":
        tu += ky_tu
    elif tu:
        print(tu)
        tu = ""
if tu:
    print(tu)