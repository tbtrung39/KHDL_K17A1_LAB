def diem_trung_binh(toan,ly,hoa):
    diem_trung_binh=(toan+ly+hoa)/3
    return diem_trung_binh
ho_ten=input("Nhập họ và tên:")
toan=float(input("Nhập điểm toán:"))
ly=float(input("Nhập điểm lý:"))
hoa=float(input("Nhập điểm hóa:"))
print("Họ và tên:",ho_ten,"Điểm toán:",toan,"Điểm hóa:",hoa,"Điểm lý:",ly,"Điểm trung bình các  môn:",diem_trung_binh(toan,ly,hoa))