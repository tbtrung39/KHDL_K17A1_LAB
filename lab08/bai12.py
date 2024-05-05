def nhap_thong_tin_nhan_vien():
    ho_ten = input("Nhập Họ và Tên của nhân viên: ")
    que_quan = input("Nhập Quê quán của nhân viên: ")
    nam_kinh_nghiem = int(input("Nhập số năm kinh nghiệm của nhân viên: "))
    return ho_ten, que_quan, nam_kinh_nghiem

def tinh_luong(nam_kinh_nghiem):
    luong_co_ban = int(input(" nhap luong co ban: "))
    phu_cap = nam_kinh_nghiem * 500000 
    luong = luong_co_ban + phu_cap
    return luong

def xuat_thong_tin_nhan_vien(ho_ten, que_quan, nam_kinh_nghiem, luong):
    print("Họ và Tên:", ho_ten)
    print("Quê quán:", que_quan)
    print("Thâm niên công tác:", nam_kinh_nghiem, "năm")
    print("Lương:", luong, "VNĐ")

ho_ten, que_quan, nam_kinh_nghiem = nhap_thong_tin_nhan_vien()
luong = tinh_luong(nam_kinh_nghiem)
xuat_thong_tin_nhan_vien(ho_ten, que_quan, nam_kinh_nghiem, luong)
