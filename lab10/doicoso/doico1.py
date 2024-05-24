def nhap_so():
    so=int(input('moi nhap so:'))
    print(f"so duoc nhap la:{so}")
    return so
def chuyen_sang_he_nhi_phan(so):
    he_nhi_phan=bin(so)[2:]
    print(f"so duoc chuyen sang he nhi phan la:{he_nhi_phan}")
    return he_nhi_phan  
def chuyen_sang_he_bat_phan(so):
    he_bat_phan=oct(so)[2:]
    print(f"he bat phan sau khi chuyen duoc la:{he_bat_phan}")
    return he_bat_phan
def chuyen_sang_he_thap_luc_phan(so):
    he_thap_luc_phan=hex(so)[2:]
    print(f"chuyen sang he thap luc phan:{he_thap_luc_phan}")
    return he_thap_luc_phan