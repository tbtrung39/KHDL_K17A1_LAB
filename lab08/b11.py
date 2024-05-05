def nhap():
    ho_ten = input("nhap ho va ten: ")
    diem_toan = float(input("nhap diem toan: "))
    diem_ly = float(input("nhap diem ly: "))
    diem_hoa = float(input("nhap diem hoa: "))
    return ho_ten, diem_toan, diem_hoa, diem_ly

def tinh_trung_binh(diem_toan, diem_ly, diem_hoa):
    diem_tb = (diem_toan + diem_ly + diem_hoa)/3
    return diem_tb

def xuat_ket_qua(ho_ten,diem_tb):
    print("ho va ten:",ho_ten)
    print("diem trung binh:",diem_tb)
    return

ho_ten, diem_toan, diem_ly, diem_hoa = nhap()
diem_tb= tinh_trung_binh(diem_toan,diem_ly,diem_hoa)
xuat_ket_qua(ho_ten,diem_tb)



