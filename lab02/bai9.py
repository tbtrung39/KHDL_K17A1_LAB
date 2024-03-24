so_kw = float(input("Nhập số KW điện tiêu thụ: "))
if 0 < so_kw <= 100:
    print("Tiền điện: ", 2000*so_kw, "VND")
elif 101 < so_kw <= 200:
    print("Tiền điện: ", 2500*so_kw, "VND")
elif 201 < so_kw <= 300:
    print("Tiền điện: ", 3000*so_kw, "VND")
else:
    print("Tiền điện: ", 5000*so_kw, "VND")