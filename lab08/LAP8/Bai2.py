def tim_ucln(a, b):
    while b:
        a, b = b, a % b
    return a

tu_so = int(input("Nhập tử số: "))
mau_so = int(input("Nhập mẫu số: "))

UCLN = tim_ucln(tu_so, mau_so)
print('Ước chung lớn nhất là:',UCLN)
# Rút gọn phân số 
tu_so_rut_gon = tu_so // UCLN
mau_so_rut_gon = mau_so // UCLN
print(f"Phân số rút gọn của {tu_so}/{mau_so} là {tu_so_rut_gon}/{mau_so_rut_gon}")