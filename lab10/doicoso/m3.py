def he_nhi_phan(n):
    if n == 0:
        return 0
    he_nhi_phan = ""
    while n > 0:
        he_nhi_phan = str(n % 2) + he_nhi_phan
        n = n // 2
    return he_nhi_phan

def he_bat_phan(n):
    if n == 0:
        return 0
    he_bat_phan = ""
    while n > 0:
        he_bat_phan = str(n % 8) + he_bat_phan
        n = n // 8
    return he_bat_phan

def he_thap_luc_phan(n):
    if n == 0:
        return "0"
    he_thap_luc_phan = ""
    hex_chars = "0123456789abcdef"
    while n > 0:
        he_thap_luc_phan = hex_chars[n % 16] + he_thap_luc_phan
        n = n // 16
    return he_thap_luc_phan

