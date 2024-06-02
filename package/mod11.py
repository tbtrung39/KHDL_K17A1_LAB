def in_ra(n):
    return n

def cs01(n):
    if n == 0:
        return '0'
    np = ''
    while n > 0:
        np = str(n % 2) + np
        n //= 2
    return np

def cs8p(n):
    if n == 0:
        return '0'
    bp = ''
    while n > 0:
        bp = str(n % 8) + bp
        n //= 8
    return bp

def cs16p(n):
    if n == 0:
        return '0'
    tlp = ''
    hex_chars = "0123456789ABCDEF"    
    while n > 0:
        re = n % 16
        tlp = hex_chars[re] + tlp
        n //= 16  
    return tlp

def xoa_kt_ko_hop_le(chuoi):
    ky_tu_hop_le = ""
    for char in chuoi:
        if char.isdigit() or ('A' <= char <= 'Z'):
            ky_tu_hop_le += char
    return ky_tu_hop_le

def cs2_to_cs10(cs2):
    cs2 = str(cs2)
    cs10 = 0
    for i in range(len(cs2) - 1, -1, -1):
        if cs2[i] == '1':
            cs10 += 2 ** (len(cs2) - 1 - i) 
    return cs10

def cs8_to_cs10(cs8):
    cs8 = str(cs8)
    cs10 = 0
    for i in range(len(cs8)):
        cs10 += int(cs8[-i - 1]) * (8 ** i)
    return cs10