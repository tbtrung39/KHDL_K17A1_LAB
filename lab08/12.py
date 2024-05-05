def thong_tin_nhan_vien():
    hoten = input("Nhập tên nhân viên:")
    que = input("Nhập quê quán:")
    tham_nien = int(input("Nhập thâm niên công tác:"))
    return hoten, que, tham_nien

def tinh_luong(tham_nien):
    luong = 100000
    if tham_nien >= 4:
        luong += 70000
    return luong

def xuat(hoten, que, tham_nien, luong):
    print("Thông tinn nhân viên :")
    print("Họ và tên nhân viên",hoten)
    print("Quê quán:",que)
    print("Thâm niên công tác:",tham_nien)
    print("Lương:",luong)


def main():
    hoten, que, tham_nien = thong_tin_nhan_vien()
    luong = tinh_luong(tham_nien)
    xuat(hoten, que, tham_nien, luong)

main()
