def ham_nhap():
    ho_ten = input("nhap ho va ten: ")
    que_quan = input("nhap que quan: ")
    tham_nien = int(input("nhap tham nien cong tac: "))
    return ho_ten, que_quan, tham_nien

def salary(tham_nien):
    luong = 10000000*tham_nien
    return luong
def xuat(ho_ten, que_quan,tham_nien,luong):
    print("ho va ten:",ho_ten)
    print("que quan:",que_quan)
    print("tham nien:",tham_nien)
    print("luong:",luong)
    return

def use_all():
    ho_ten, que_quan, tham_nien = ham_nhap()
    luong = salary(tham_nien)
    xuat(ho_ten,que_quan,tham_nien,luong)
    return

use_all()