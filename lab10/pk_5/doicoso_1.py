def nhap_so_nguyen():
    so_nguyen = int(input("Nhập số nguyên: "))
    print("Số nguyên bạn vừa nhập là:", so_nguyen)
    return so_nguyen

def chuyen_doi_nhi_phan(so_nguyen):
    print("Số nhị phân của", so_nguyen, "là:", bin(so_nguyen))

def chuyen_doi_co_so_8(so_nguyen):
    print("Số cơ số 8 của", so_nguyen, "là:", oct(so_nguyen))

def chuyen_doi_co_so_16(so_nguyen):
    print("Số cơ số 16 của", so_nguyen, "là:", hex(so_nguyen))
