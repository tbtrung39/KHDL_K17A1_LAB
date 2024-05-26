def so_nguyen():
    n = int(input("nhap vao mot so nguyen: "))
    print("so nguyen vua nhap la: ",n)
    return n
def chuyen_doi_nhi_phna(n):
    nhi_phan = bin(n)[2:]
    print(f'so {n} trong he nhi phan la: {nhi_phan}')
def chuyen_doi_bat_phan(n):
    bat_phan = oct(n)[2:]
    print(f'so {n} trong he bat phat la: {bat_phan}')
def chuyen_doi_thap_luc_phan(n):
    thap_luc_phan = hex(n)[2:]
    print(f"so {n} trong he thap luc phhan la: {thap_luc_phan}")