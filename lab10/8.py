from pk_8 import Matranvuong
matrix = Matranvuong.nhap_matran()
Matranvuong.in_matran(matrix)
Matranvuong.chuyen_vi(matrix)
if Matranvuong.kiem_tra_doi_xung(matrix):
    print("Ma trận là ma trận đối xứng.")
else:
    print("Ma trận không phải là ma trận đối xứng.")
