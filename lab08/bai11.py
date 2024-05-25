def nhap_thong_tin_sinh_vien():
    ho_ten = input("nhap ho ten SV: ")
    diem_toan = float(input("nhap diem toan: "))
    diem_ly = float(input("nhap diem ly: "))
    diem_hoa = float(input("nhap diem hoa: "))
    return ho_ten, diem_toan, diem_ly, diem_hoa

def tinh_diem_trung_binh(diem_toan, diem_ly, diem_hoa):
    diem_tb = (diem_toan + diem_ly + diem_hoa) / 3
    return diem_tb

def xuat_ket_qua(ho_ten, diem_tb):
    print("ho va ten", ho_ten)
    print("Đdiem trung binh:", diem_tb)

ho_ten, diem_toan, diem_ly, diem_hoa = nhap_thong_tin_sinh_vien()
diem_tb = tinh_diem_trung_binh(diem_toan, diem_ly, diem_hoa)
xuat_ket_qua(ho_ten, diem_tb)
