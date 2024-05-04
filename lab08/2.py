#2
def ucln(a, b):
    while b:
        a, b = b, a % b
    return a

def rut_gon_phan_so(tu, mau):
    ucln_phan_so = ucln(tu, mau)
    tu_rut_gon = tu // ucln_phan_so
    mau_rut_gon = mau // ucln_phan_so
    return tu_rut_gon, mau_rut_gon

tu_so = int(input("Nhập tử số của phân số: "))
mau_so = int(input("Nhập mẫu số của phân số: "))

tu_rut_gon, mau_rut_gon = rut_gon_phan_so(tu_so, mau_so)

print("Phân số sau khi được rút gọn là:", tu_rut_gon, "/", mau_rut_gon)