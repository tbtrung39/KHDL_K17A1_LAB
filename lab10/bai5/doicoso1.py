def doiso(a):
    return a
def henhiphan(a):
    if a == 0:
        return "0"
    chuyendoiso = ""
    while a > 0:
        chuyendoiso = str(a % 2) + chuyendoiso
        a = a // 2
    return chuyendoiso
 
def chuyen_doi_thap_phan_sang_bat_phan(a):
    if a == 0:
        return "0"   
    mang_bat_phan = []
    while a > 0:
        mang_bat_phan.append(str(a % 8))
        a = a // 8
    return "".join(mang_bat_phan[::-1])
