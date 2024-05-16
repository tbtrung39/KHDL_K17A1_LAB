def nhap_so():
    n=int(input("nhap so nguyen: "))
    return n

def chuyen_sang_he_nhi_phan(n):
    return bin(n)[2:]

def chuyen_sang_he_bat_phan(n):
    if n==0:
        return '0'
    bat_phan=''
    while n>0:
        bat_phan=str(n%8)+bat_phan
        n=n//8
    return bat_phan

def chuyen_sang_he_16(n):
    return hex(n)[2:].upper()