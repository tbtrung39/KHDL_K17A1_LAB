def uoc_chung_lon_nhat(a, b):
    if b == 0:
        return a
    return uoc_chung_lon_nhat(b, a % b)
so1 = int(input("Nhập số thứ nhất: "))
so2 = int(input("Nhập số thứ hai: "))
ucln = uoc_chung_lon_nhat(so1, so2)
print("Ước chung lớn nhất của {0} và {1} là: {2}".format(so1, so2, ucln)) # là phương thức dùng để định dạng chuỗi
