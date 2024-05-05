def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def rut_gon_phan_so(tu, mau):
    ucln_tu_mau = ucln(tu, mau)
    tu = tu // ucln_tu_mau
    mau = mau // ucln_tu_mau
    return tu, mau

tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))

tu_rut_gon, mau_rut_gon = rut_gon_phan_so(tu, mau)
print("Phân số sau khi rút gọn là: {}/{}".format(tu_rut_gon, mau_rut_gon))
# hàm format dùng để định dạng chuỗi hoặc định dạng lại các chuỗi được đề xuất ra 
