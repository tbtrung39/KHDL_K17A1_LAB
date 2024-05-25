def nhap_so():
    n = int(input("Nhập vào một số nguyên: "))
    return n

def doi_sang_nhi_phan(n):
    return bin(n)[2:]

def doi_sang_bat_phan(n):
    return oct(n)[2:]

def doi_sang_thap_luc_phan(n):
    return hex(n)[2:]