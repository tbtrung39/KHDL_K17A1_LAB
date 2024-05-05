def f():
    ten = input("nhập họ và tên sinh viên:")
    toan = int(input("nhập điểm toán:"))
    ly = int(input("nhập điểm lý:"))
    hoa = int(input("nhập điểm hóa:"))

    if toan >= 0 and ly >= 0 and hoa >= 0:
        diemtb = (toan + ly + hoa)/3
        print("Sinh viên:", ten, "có điểm trung bình là:",diemtb) 
        

    else:
        print("Sai")
    
    return

f()

