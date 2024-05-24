
from package_8 import Matranvuong

def main():
    n = int(input("Nhập kích thước của ma trận vuông N: "))
    
    ma_tran = Matranvuong.nhap_ma_tran(n)
    Matranvuong.in_ma_tran(ma_tran)
    
    Matranvuong.ma_tran_chuyen_vi(ma_tran)
    
    doi_xung = Matranvuong.kiem_tra_doi_xung(ma_tran)
    if doi_xung:
        print("Ma trận đối xứng: True")
    else:
        print("Ma trận đối xứng: False")

if __name__ == "__main__":
    main()