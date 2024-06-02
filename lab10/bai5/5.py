import doicoso1

def main():
    so = doicoso1.nhap_so_nguyen()
    print(f"Số vừa nhập: {so}")

    nhi_phan = doicoso1.chuyen_doi_nhi_phan(so)
    print(f"Số {so} ở hệ nhị phân: {nhi_phan}")

    co_so_8 = doicoso1.chuyen_doi_co_so_8(so)
    print(f"Số {so} ở hệ cơ số 8: {co_so_8}")

    co_so_16 = doicoso1.chuyen_doi_co_so_16(so)
    print(f"Số {so} ở hệ cơ số 16: {co_so_16}")

if __name__ == "__main__":
    main()
