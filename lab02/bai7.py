diem=int(input("nhập điểm của học sinh để xếp loại : "))
if diem<3:
    print("Loại Kém")
elif diem ==4 :
    print("Loại Yếu ")
elif diem >=5 and diem<=6:
    print("Loại Trung Bình ")
elif diem>=7 and diem<=8 :
    print("Loại Khá")
elif diem>=9 and diem<=10:
    print("Loại Giỏi")
else:
    print("điểm không hợp lệ ")
