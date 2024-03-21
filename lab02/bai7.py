# Nhập điểm trung bình từ người dùng
diem = float(input("Nhập điểm trung bình: "))

# Kiểm tra và in ra học lực tương ứng
if diem >= 0 and diem < 4:
    print("Loại Kém")
elif diem == 4:
    print("Loại Yếu")
elif diem >= 5 and diem < 7:
    print("Loại Trung bình")
elif diem >= 7 and diem < 9:
    print("Loại Khá")
elif diem >= 9 and diem <= 10:
    print("Loại Giỏi")
else:
    print("Điểm không hợp lệ")