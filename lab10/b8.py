import sys
sys.path.append("lab10\packages")
import packages
a = int(input("Nhap cot cua ma tran:"))
n = int(input("Nhap hang cua ma tran:"))
matran = packages.nhap_ma_tran(a,n)
print("Ma trận vừa nhập là:")
packages.in_ma_tran(matran)
print("ma trận chuyển vị:")
packages.in_ma_tran(packages.ma_tran_chuyen_vi(matran))
if packages.kiem_tra_doi_xung(matran):
    print("Ma trận đối xứng")
else:
    print("Ma trận không đối xứng")