def nhap_thong_tin():
    ho_ten = input("nhập họ và tên:")
    que_quan = input("nhập quê quán:")
    tham_nien_ct = int(input("nhập thâm niên công tác của công nhân:"))
    return ho_ten, que_quan , tham_nien_ct

def luong_tham_nien_cong_tac():
    tham_nien_cong_tac = int(input("nhập thâm niên công tác:"))
    if tham_nien_cong_tac == 6:
        luong = tham_nien_cong_tac * 500
    if tham_nien_cong_tac == 12:
        luong = tham_nien_cong_tac * 1000
    return luong

