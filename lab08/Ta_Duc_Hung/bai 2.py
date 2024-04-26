def ucln(x,y):
    while y!= 0:
        x,y = x , x % y
        return x

def rutgon(a, b):
    Ucln = ucln(a, b)
    rg_a = a / Ucln
    rg_b = b / Ucln
    return rg_a, rg_b

tu_so = int(input("Nhập tử số: "))
mau_so = int(input("Nhập mẫu số: "))

tu_rut_gon, mau_rut_gon = rutgon(tu_so, mau_so)

print( tu_rut_gon, "/", mau_rut_gon) 