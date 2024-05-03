ho_ten = input("Nhap ho ten sinh vien: ")
def tinh_diem_trung_binh(toan, ly, hoa):
    diem_trung_binh = (toan + ly + hoa) / 3
    return diem_trung_binh
toan = float(input("Nhap diem toan: "))
ly = float(input("Nhap diem ly: "))
hoa = float(input("Nhap diem hoa: "))
diem_trung_binh = tinh_diem_trung_binh(toan, ly, hoa)
print("Diem trung binh cua sinh vien", ho_ten, "la:", diem_trung_binh)
