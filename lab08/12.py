def nhap_thong_tin_nhan_vien():
    ho_ten = input("tên nv: ")
    que_quan = input("quên quán: ")
    tham_nien = int(input("thời gian làm việc: "))
    return ho_ten, que_quan, tham_nien

def tinh_luong(tham_nien):
    luong = 1000000  
    if tham_nien >= 5:
        luong += 50000 
    return luong

def xuat(ho_ten, que_quan, tham_nien, luong):
    print("Thông tin nhân viên:")
    print("Họ và tên:", ho_ten)
    print("Quê quán:", que_quan)
    print("Thâm niên công tác:", tham_nien, "năm")
    print("Lương:", luong, "VND")

def main():
    ho_ten, que_quan, tham_nien = nhap_thong_tin_nhan_vien()
    luong = tinh_luong(tham_nien)
    xuat(ho_ten, que_quan, tham_nien, luong)

main()
