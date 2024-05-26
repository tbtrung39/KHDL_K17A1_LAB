def nhap_va_in_so_nguyen():
    so_nguyen = int(input("Nhập vào một số nguyên: "))
    print("Số nguyên bạn vừa nhập là:", so_nguyen)

def chuyen_doi_nhi_phan(so_nguyen):
    print("Số nhị phân tương ứng là:", bin(so_nguyen))

def chuyen_doi_bat_phan(so_nguyen):
    print("Số bát phân tương ứng là:", oct(so_nguyen))

def chuyen_doi_thap_luc_phan(so_nguyen):
    print("Số thập lục phân tương ứng là:", hex(so_nguyen))
