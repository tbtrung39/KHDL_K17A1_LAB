def tim_uoc_chung_lon_nhat(a, b):
    while b != 0:
        a, b = b, a % b
    return a
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
ucln = tim_uoc_chung_lon_nhat(a, b)
print("Uoc chung lon nhat:", ucln)
