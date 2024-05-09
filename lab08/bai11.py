def nhap_thong_tin():
    ho_va_ten = input("nhập họ và tên:")
    diem_toan = int(input("nhập điểm toán của sinh viên:"))
    diem_ly = int(input("nhập điểm lý của sinh viên:"))
    diem_hoa = int(input("nhập điểm hóa của sinh viên:"))
    return ho_va_ten,diem_toan,diem_ly,diem_hoa

def diem_trung_binh(diem_toan,diem_ly,diem_hoa):
    dtb = (diem_toan+diem_ly+diem_hoa)/3
    print(f"điểm trung bình của sinh viên là:{dtb}")
    return dtb

ho_ten, diem_toan, diem_ly, diem_hoa = nhap_thong_tin()

diem_tb = diem_trung_binh(diem_toan, diem_ly, diem_hoa)
