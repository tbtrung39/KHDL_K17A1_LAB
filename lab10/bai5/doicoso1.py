def nhap_so_nguyen():
    while True:
        try:
            so = int(input("Nhập vào một số nguyên: "))
            return so
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")

def chuyen_doi_nhi_phan(so):
    return bin(so)

def chuyen_doi_co_so_8(so):
    return oct(so)

def chuyen_doi_co_so_16(so):
    return hex(so)
