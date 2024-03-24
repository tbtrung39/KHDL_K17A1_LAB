diem_tk = float(input("Nhập điểm tổng kết: "))
if 0 <= diem_tk < 3:
    print("Loại kém")
elif diem_tk == 4: 
    print("Loại yếu ")
elif 5 <= diem_tk <= 6:
    print("Loại trung bình")
elif 7 <= diem_tk <= 8:
    print("Loại khá")
elif 9 <= diem_tk <= 10:
    print("Loại giỏi")
else:
    print("Nhập điểm không hợp lệ!")