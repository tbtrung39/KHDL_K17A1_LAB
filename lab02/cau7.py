diem = float(input("Nhập điểm tổng kết của học sinh: "))

if diem >= 0.0 and diem < 4.0:
    print("Học lực: Loại Kém")
elif diem == 4.0:
    print("Học lực: Loại Yếu")
elif diem >= 5.0 and diem < 7.0:
    print("Học lực: Loại Trung bình")
elif diem >= 7.0 and diem < 9.0:
    print("Học lực: Loại Khá")
elif diem >= 9.0 and diem <= 10.0:
    print("Học lực: Loại Giỏi")
else:
    print("Điểm không hợp lệ. Vui lòng nhập điểm từ 0.0 đến 10.0")