def ucln(x,y):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x
tu_so = int(input("Nhập tử số: "))
mau_so = int(input("Nhập mẫu số: "))
tu_rut_gon = tu_so // ucln(tu_so, mau_so)
mau_rut_gon = mau_so // ucln(tu_so,mau_so)
print(f"{tu_rut_gon}/{mau_rut_gon}") 