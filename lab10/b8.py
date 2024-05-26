from pk_b8 import Matranvuong
def main():
    while True:
        try:
            n = int(input("Nhập kích thước của ma trận NxN: "))
            if n <= 0:
                raise ValueError("Kích thước phải là một số nguyên dương.")
            break
        except ValueError as e:
            print(e)
    
    print(f"Nhập ma trận {n}x{n}:")
    ma_tran = Matranvuong.nhap_ma_tran(n)
    
    print("Ma trận đã nhập:")
    Matranvuong.in_ma_tran(ma_tran)
    
    ma_tran_chuyen_vi = Matranvuong.tinh_ma_tran_chuyen_vi(ma_tran)
    print("Ma trận chuyển vị:")
    Matranvuong.in_ma_tran(ma_tran_chuyen_vi)
    
    doi_xung = Matranvuong.kiem_tra_doi_xung(ma_tran)
    if doi_xung:
        print("Ma trận này là ma trận đối xứng.")
    else:
        print("Ma trận này không phải là ma trận đối xứng.")

if __name__ == "__main__":
    main()
