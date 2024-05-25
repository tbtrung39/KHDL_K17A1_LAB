import Matranvuong
kich_thuoc = int(input("Nhập kích thước của ma trận vuông: "))
matran = Matranvuong.nhap_matran(kich_thuoc)
Matranvuong.in_matran(matran)
chuyen_vi_matran = Matranvuong.chuyen_vi(matran, kich_thuoc)
print("Ma trận chuyển vị:")
for hang in chuyen_vi_matran:
    print(hang)
if Matranvuong.kiem_tra_doi_xung(matran, kich_thuoc):
    print("Ma trận là ma trận đối xứng.")
else:
    print("Ma trận không là ma trận đối xứng.")