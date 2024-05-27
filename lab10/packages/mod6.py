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