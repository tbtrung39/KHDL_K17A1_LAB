from pk_b5 import doicoso1
def main():
    doicoso1.nhap_va_in_so_nguyen()

    so_nguyen = int(input("Nhập một số nguyên để chuyển đổi: "))

    doicoso1.chuyen_doi_nhi_phan(so_nguyen)

    doicoso1.chuyen_doi_bat_phan(so_nguyen)

    doicoso1.chuyen_doi_thap_luc_phan(so_nguyen)

if __name__ == "__main__":
    main()
