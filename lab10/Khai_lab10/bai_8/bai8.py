from package_8 import Matranvuong as m

n = int(input("Nhập kích thước của ma trận vuông: "))

ma_tran = m.nhap_ma_tran(n)
m.in_ma_tran(ma_tran)
print("Ma trận chuyển vị là:")
m.in_ma_tran(m.ma_tran_chuyen_vi(ma_tran))

if m.kiem_tra_ma_tran_doi_xung(ma_tran):
    print("Ma trận là ma trận đối xứng.")
else:
    print("Ma trận không phải là ma trận đối xứng.")
