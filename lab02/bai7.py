diem_TK=float(input("Nhập điểm ổng kết của mottj học sinh: "))
if diem_TK<0 or diem_TK >10:
    print("điểm không hợp lệ!!!")
elif diem_TK>0.0 and diem_TK <=3.0:
    print("loại kém")
elif diem_TK >3.0 and diem_TK <5.0:
    print("loại yếu")
elif diem_TK >=5 and diem_TK<7:
    print("loại trung bình")
elif diem_TK>=7 and diem_TK <9:
    print("loại khá")
elif diem_TK>9 and diem_TK <=10:
    print("loại giỏi")