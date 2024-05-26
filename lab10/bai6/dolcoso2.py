def loai_bo_ky_tu_khong_hop_le(chuoi):
    ky_tu_hop_le = "0123456789ABCDEF"
    ket_qua = ''.join(ky_tu for ky_tu in chuoi if ky_tu.upper() in ky_tu_hop_le)
    print("Chuỗi kết quả sau khi loại bỏ các ký tự không hợp lệ:", ket_qua)
    return ket_qua

def xac_dinh_co_so(chuoi):
    if all(ky_tu in "01" for ky_tu in chuoi):
        co_so = 2
    elif all(ky_tu in "01234567" for ky_tu in chuoi):
        co_so = 8
    elif all(ky_tu.upper() in "0123456789ABCDEF" for ky_tu in chuoi):
        co_so = 16
    else:
        co_so = 10
    print(f"Chuỗi số '{chuoi}' có cơ số {co_so}")
    return co_so

def chuyen_co_so2_sang_co_so10(chuoi_nhi_phan):
    gia_tri_thap_phan = int(chuoi_nhi_phan, 2)
    print(f"Chuỗi nhị phân '{chuoi_nhi_phan}' chuyển sang cơ số 10 là {gia_tri_thap_phan}")
    return gia_tri_thap_phan

def chuyen_co_so8_sang_co_so10(chuoi_bat_phan):
    gia_tri_thap_phan = int(chuoi_bat_phan, 8)
    print(f"Chuỗi bát phân '{chuoi_bat_phan}' chuyển sang cơ số 10 là {gia_tri_thap_phan}")
    return gia_tri_thap_phan

def chuyen_co_so16_sang_co_so10(chuoi_thap_luc_phan):
    gia_tri_thap_phan = int(chuoi_thap_luc_phan, 16)
    print(f"Chuỗi thập lục phân '{chuoi_thap_luc_phan}' chuyển sang cơ số 10 là {gia_tri_thap_phan}")
    return gia_tri_thap_phan
