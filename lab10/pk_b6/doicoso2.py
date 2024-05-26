def loai_bo_ky_tu_khong_hop_le(chuoi):
    """Loại bỏ tất cả các ký tự không thuộc vào tập hợp {0-9, A-F}"""
    ky_tu_hop_le = set('0123456789ABCDEF')
    chuoi_sach = ''.join(filter(lambda x: x in ky_tu_hop_le, chuoi.upper()))
    return chuoi_sach

def phat_hien_co_so(chuoi):
    """Cho biết chuỗi số cho trước là biểu diễn cơ số mấy"""
    chuoi = chuoi.upper()
    if all(c in '01' for c in chuoi):
        return 2
    elif all(c in '01234567' for c in chuoi):
        return 8
    elif all(c in '0123456789ABCDEF' for c in chuoi):
        return 16
    elif all(c in '0123456789' for c in chuoi):
        return 10
    else:
        return -1

def doi_co_so_2_sang_10(chuoi_nhi_phan):
    """Chuyển đổi một chuỗi số từ cơ số 2 sang cơ số 10"""
    return int(chuoi_nhi_phan, 2)

def doi_co_so_8_sang_10(chuoi_bat_phan):
    """Chuyển đổi một chuỗi số từ cơ số 8 sang cơ số 10"""
    return int(chuoi_bat_phan, 8)

def doi_co_so_16_sang_10(chuoi_thap_luc_phan):
    """Chuyển đổi một chuỗi số từ cơ số 16 sang cơ số 10"""
    return int(chuoi_thap_luc_phan, 16)
