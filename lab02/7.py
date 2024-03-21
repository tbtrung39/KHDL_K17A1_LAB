n = float(input("Nhập điểm hệ : "))
if n > 10 and n < 0:
    print("Điểm nhập không hợp lệ")
else:
    if n >= 0 and n < 3:
        print("Kém")
    elif n >= 3 and n < 5:
        print("Yếu")
    elif n >= 5  and n < 7:
        print("Trung bình")
    elif n >= 7 and n < 9:
        print("Khá")
    else:
        print("Giỏi")