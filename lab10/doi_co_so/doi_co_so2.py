def nhap_va_loc_chuoi():
    chuoi_dau_vao = input('Nhập chuỗi: ').upper()
    tap_hop = set('0123456789ABCDEF')
    chuoi_hop_le = ''.join([ky_tu for ky_tu in chuoi_dau_vao if ky_tu in tap_hop])
    return chuoi_hop_le

def xac_dinh_co_so(chuoi_hop_le):
    tap_nhi_phan = set('01')
    tap_bat_phan = set('01234567')
    tap_thap_phan = set('0123456789')
    tap_16 = set('0123456789ABCDEF')
    chuoi_set = set(chuoi_hop_le)
    if chuoi_set.issubset(tap_nhi_phan):
        return 2
    if chuoi_set.issubset(tap_bat_phan):
        return 8
    if chuoi_set.issubset(tap_thap_phan):
        return 10
    if chuoi_set.issubset(tap_16):
        return 16
    else:
        return "Chuỗi không hợp lệ"

def chuyen_co_so_2_sang_co_so_10(chuoi_hop_le):
    if xac_dinh_co_so(chuoi_hop_le) == 2:
        so_thap_phan = int(chuoi_hop_le, 2)
        print("Số thập phân là: ", so_thap_phan)
    else:
        return None
    
def chuyen_co_so_8_sang_co_so_10(chuoi_hop_le):
    if xac_dinh_co_so(chuoi_hop_le) == 8:
        so_thap_phan = int(chuoi_hop_le, 8)
        print("Số thập phân là: ", so_thap_phan)
    else:
        return None
    
def chuyen_co_so_16_sang_co_so_10(chuoi_hop_le):
    if xac_dinh_co_so(chuoi_hop_le) == 16:
        so_thap_phan = int(chuoi_hop_le, 16)
        print("Số thập phân là: ", so_thap_phan)
    else:
        return None