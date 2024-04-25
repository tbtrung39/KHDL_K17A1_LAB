#thuật toán euclid ta cho a = b , b = phần dư của a / b đến khi nào phép dư bằng 0 thì trả về giá trị a
#a là ước chung lớn nhất sau khi trả về
def tim_ucln(a, b):
    #Tìm ước chung lớn nhất của hai số a và b.
    while b != 0:
        a, b = b, a % b
    return a
def rut_gon_phan_so(tu_so, mau_so):
    #Rút gọn phân số bằng cách chia tử và mẫu cho ước chung lớn nhất
    ucln = tim_ucln(tu_so, mau_so)
    tu_so_rut_gon = tu_so // ucln
    mau_so_rut_gon = mau_so // ucln
    return tu_so_rut_gon, mau_so_rut_gon

tu_so = int(input("Nhập tử số: "))
mau_so = int(input("Nhập mẫu số: "))

tu_so_rut_gon, mau_so_rut_gon = rut_gon_phan_so(tu_so, mau_so)
print(f"Phân số sau khi rút gọn là: {tu_so_rut_gon} /  {mau_so_rut_gon}")