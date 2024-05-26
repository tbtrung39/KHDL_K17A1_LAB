def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def rut_gon(tu, mau):
    tu_moi = tu // ucln(tu,mau)
    mau_moi = mau//  ucln(tu, mau)
    return tu_moi, mau_moi

# Nhập tử số và mẫu số từ người dùng
tu= int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))
tu_moi, mau_moi = rut_gon(tu, mau)
print("Phân số rút gọn:", tu_moi, "/", mau_moi)