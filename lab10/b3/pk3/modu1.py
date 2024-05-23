def uoc_chung_lon_nhat(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def boi_chung_nho_nhat(a, b):
    ucln = uoc_chung_lon_nhat(a, b)
    bcnn = (a * b) // ucln
    return bcnn
