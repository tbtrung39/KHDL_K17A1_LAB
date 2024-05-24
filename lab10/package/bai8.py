from __pycache__ import matranvuong
n = int(input('Nhap kich thuoc cua ma tran vuong: '))
a = matranvuong.nhap_du_lieu(n)
print(a)
matranvuong.in_matrix(a)
matranvuong.ma_tran_chuyen_vi(a)
print(matranvuong.kiem_tra_doi_xung(a))