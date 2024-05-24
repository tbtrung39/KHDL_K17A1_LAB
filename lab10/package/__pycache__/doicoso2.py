def loai_ky_tu(b):
    a=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    k =''
    for i in b:
        if i.upper() in a:
            k+=i
    return k
def he2_sang_he10(a):
    return int(a, 2)
def he8_sang_he10(a):
    return int(a, 8)
def he16_sang_he10(a):
    return int(a, 16)