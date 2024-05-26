def loc_ki_tu(chuoi):
    hop_le = set("0123456789ABCDEF")
    ket_qua=''.join(h for h in chuoi if h in hop_le)
    print("chuoi sau khi loc:",ket_qua)
    return ket_qua
def xac_dinh_co_so(chuoi):
    if all(h in '01' for h in chuoi):
        print(f"chuoi {chuoi} la bieu dien cua he co so 2")
        return 2
    elif all(h in '01234567' for h in chuoi):
        print(f"chuoi {chuoi} la bieu dien cua he co so 8")
        return 8
    elif all(h in '0123456789ABCDEF' for h in chuoi):
        print(f"chuoi {chuoi} la bieu dien he co so 16")
        return 16
    else:
        print(f"chuoi {chuoi} khong phai la bieu dien he co so 2,8,16")
        return 
def chuyen_doi_nhi_phan_sang_thap_phan(chuoi):
    return int(chuoi,2)
def chuyen_doi_bat_phan_sang_thap_phan(chuoi):
    return int(chuoi,8)
def chuyen_doi_thap_luc_phan_sang_thap_phan(chuoi):
    return int(chuoi,16)