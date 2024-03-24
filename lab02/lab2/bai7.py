diem_tong_ket= float(input("Nhập điểm tk: "))
if diem_tong_ket > 10 or diem_tong_ket < 0:
    print("Không hợp lệ!!!")
else:
    if diem_tong_ket >= 9.0 and  diem_tong_ket <= 10.0 :
        print("Học lực: Giỏi")
    elif diem_tong_ket >= 7.0:
        print("Học lực: Khá")
    elif diem_tong_ket >= 5.0:
        print("Học lực: Trung bình")
    elif diem_tong_ket >= 4.0:
        print("Học lực: Yếu")
    else:
        print("Học lực: Kém")