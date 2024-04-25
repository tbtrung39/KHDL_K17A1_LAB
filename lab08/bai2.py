def ucln(a, b):
    """Hàm tìm UCLN của hai số a và b."""
    while b != 0:
        a, b = b, a % b
    return a

def rut_gon_phan_so(tu_so, mau_so):
    """Hàm rút gọn phân số."""
    ucln_cua_phan_so = ucln(tu_so, mau_so)
    tu_so_rut_gon = tu_so // ucln_cua_phan_so
    mau_so_rut_gon = mau_so // ucln_cua_phan_so
    return tu_so_rut_gon, mau_so_rut_gon

# Nhập tử số và mẫu số từ người dùng
tu_so = int(input("Nhập tử số của phân số: "))
mau_so = int(input("Nhập mẫu số của phân số: "))

# Kiểm tra mẫu số phải khác 0
if mau_so == 0:
    print("Mẫu số phải khác 0.")
else:
    # Rút gọn phân số
    tu_so_rut_gon, mau_so_rut_gon = rut_gon_phan_so(tu_so, mau_so)
    print(f"Phân số rút gọn là: {tu_so_rut_gon}/{mau_so_rut_gon}")