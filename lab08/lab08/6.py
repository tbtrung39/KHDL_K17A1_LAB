def tim_uoc_chung_lon_nhat(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def tim_boi_chung_nho_nhat(a, b):
    ucln = tim_uoc_chung_lon_nhat(a, b)
    bcnn = (a * b) // ucln
    return bcnn
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
bcnn = tim_boi_chung_nho_nhat(a, b)
print("Boi chung nho nhat la:", bcnn)
