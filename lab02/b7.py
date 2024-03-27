n = int(input("Nhập điểm hệ : "))
if n > 10 or n < 0:
    print("Sai")
if n >= 0 and n < 3:
    print("Kém")
if n >= 3 and n <4:
    print("Yếu")
if n >=4  and n <7:
    print("Trung bình")
if n >= 7 and n < 8:
    print("Khá")
if n >= 8 and n < 10:
    print("Giỏi")