def nhap_va_in_so_nguyen():
    so_nguyen = int(input("Nhập một số nguyên: "))
    print(f"Số nguyên đã nhập: {so_nguyen}")
    return so_nguyen

def chuyen_sang_nhi_phan(so_nguyen):
    nhi_phan = bin(so_nguyen)[2:]
    print(f"Số {so_nguyen} trong hệ nhị phân: {nhi_phan}")
    return nhi_phan

def chuyen_sang_bat_phan(so_nguyen):
    bat_phan = oct(so_nguyen)[2:]
    print(f"Số {so_nguyen} trong hệ bát phân: {bat_phan}")
    return bat_phan

def chuyen_sang_thap_luc_phan(so_nguyen):
    thap_luc_phan = hex(so_nguyen)[2:].upper()
    print(f"Số {so_nguyen} trong hệ thập lục phân: {thap_luc_phan}")
    return thap_luc_phan
