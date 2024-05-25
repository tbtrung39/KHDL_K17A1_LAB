def nhap_thong_tin_nhan_vien():
    ho_ten = input("nhap ho ten NV: ")
    que_quan = input("nhap que quan: ")
    tham_nien = int(input("nhap tham nien: "))
    return ho_ten, que_quan, tham_nien

def tinh_luong(tham_nien):
    luong= 1000000*tham_nien
    return luong

def xuat_thong_tin(ho_ten, que_quan, tham_nien, luong):
    print("ho ten NV:", ho_ten)
    print("quen quan:", que_quan)
    print("tham nien:", tham_nien)
    print("luong:", luong)

def su_dung():
    ho_ten,que_quan,tham_nien = nhap_thong_tin_nhan_vien()
    luong=tinh_luong(tham_nien)
    xuat_thong_tin(ho_ten, que_quan, tham_nien, luong)

su_dung()