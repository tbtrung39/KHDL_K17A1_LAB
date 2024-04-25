def input():
    ho_ten = input("Tên: ")
    diem_toan = float(input("Điểm Toán: "))
    diem_ly = float(input("Điểm Lý: "))
    diem_hoa = float(input("Điểm Hóa: "))
    return ho_ten, diem_toan, diem_ly, diem_hoa

def trung_binh(diem_toan, diem_ly, diem_hoa):
    diem_trung_binh = (diem_toan + diem_ly + diem_hoa) / 3
    return diem_trung_binh

def xuat(ho_ten, diem_trung_binh):
    print("Họ tên sinh viên:", ho_ten)
    print("Điểm trung bình:", diem_trung_binh)

ho_ten, diem_toan, diem_ly, diem_hoa = input()
diem_tb = trung_binh(diem_toan, diem_ly, diem_hoa)
xuat(ho_ten, diem_tb)
