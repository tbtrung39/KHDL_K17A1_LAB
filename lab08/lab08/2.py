def uoc_chung_lon_nhat(a, b):
    while b:
        a, b = b, a % b
    return a
def phan_so_rut_gon(tu_so, mau_so):
    gcd = uoc_chung_lon_nhat(tu_so, mau_so)
    tu_so //= gcd
    mau_so //= gcd
    return tu_so, mau_so
tu_so = int(input("Nhap tu so: "))
mau_so = int(input("Nhap mau so: "))
tu_so_rut_gon, mau_so_rut_gon = phan_so_rut_gon(tu_so, mau_so)
print("Phan so rut gon la:", tu_so_rut_gon, "/", mau_so_rut_gon)
