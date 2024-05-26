def nhap_thong_tin():
    n= int(input("nhap so mat hang muon nhap: "))
    thong_tin = []
    count = 0
    while count <n:
        danh_sach= []
        ma_hang = input("nhap ma hang: ")
        ten_hang = input("nhap ten hang: ")
        don_vi_tinh = input("nhap don vi tinh: ")
        don_gia = int(input("nhap don gia: "))
        so_luong = int(input("nhap so luong: "))
        thanh_tien = don_gia*so_luong
        thue = thanh_tien*(10/100)
        danh_sach.append(ma_hang)
        danh_sach.append(ten_hang)
        danh_sach.append(don_vi_tinh)
        danh_sach.append(don_gia)
        danh_sach.append(so_luong)
        danh_sach.append(thanh_tien)
        danh_sach.append(thue)
        thong_tin.append(danh_sach)
        count+=1
    return thong_tin
def sap_xep(thong_tin):
    sorted_data = sorted(thong_tin,key = lambda x: x[6],reverse=True)
    print(sorted_data)
    return