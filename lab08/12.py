def nhap_thng_tin_nv():
    ten = input("Nhập họ và tên: ")
    quequan = input("Nhập quê quán: ")
    nam_tham_nien = int(input("Nhập số năm thâm niên: "))
    thng_tin_nv = {
        "Tên": ten,
        "Quê quán": quequan,
        "Năm thâm niên": nam_tham_nien
    }
    return thng_tin_nv
def tinh_lu0ng(lu0ng, nam_tham_nien):
    if nam_tham_nien< 5:
        lu0ng_tang= 0.05
    elif nam_tham_nien < 10:
        lu0ng_tang = 0.1
    else:
        lu0ng_tang = 0.15
        
    tien_lu0ng= lu0ng * (1 +lu0ng_tang)
    return tien_lu0ng
thg_tin_nv= nhap_thng_tin_nv()
lu0ng = 5000000
tien_lu0ng = tinh_lu0ng(lu0ng, thg_tin_nv["Năm thâm niên"])
print(f"Họ và tên: {thg_tin_nv['Tên']}")
print(f"Quê quán: {thg_tin_nv['Quê quán']}")
print(f"Số năm thâm niên: {thg_tin_nv['nam_tham_nien']}")
print(f"Mức lương tính toán: {tien_lu0ng:.2f} VND")