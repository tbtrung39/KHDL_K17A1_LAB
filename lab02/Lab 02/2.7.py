diem_tk = float(input("Nhập điểm thường kỳ:"))
if 0.0 <= diem_tk <= 3.0:
    print("Loại kém")
elif diem_tk <= 4.0:
    print("Loại yếu")
elif diem_tk <= 6.0:
    print("Loại trung bình")
elif diem_tk <= 8.0:
    print("Loại khá")
elif diem_tk <= 10.0:
    print("Loại giỏi")