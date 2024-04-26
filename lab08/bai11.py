def nhap_thong_tin_sinh_vien():
    ho_ten = input("Nhập họ tên SV: ")
    diem_toan = float(input("Nhập điểm toán: "))
    diem_ly = float(input("Nhập điểm lý: "))
    diem_hoa = float(input("Nhập điểm hóa: "))
    return ho_ten, diem_toan, diem_ly, diem_hoa

def tinh_diem_trung_binh(diem_toan, diem_ly, diem_hoa):
    diem_tb = (diem_toan + diem_ly + diem_hoa) / 3
    return diem_tb

def xuat_ket_qua(ho_ten, diem_tb):
    print("Họ và tên:", ho_ten)
    print("Điểm trung bình:", diem_tb)

ho_ten, diem_toan, diem_ly, diem_hoa = nhap_thong_tin_sinh_vien()
diem_tb = tinh_diem_trung_binh(diem_toan, diem_ly, diem_hoa)
xuat_ket_qua(ho_ten, diem_tb)
