diem_Tk= float(input("nhap diem tong ket: "))
if diem_Tk >10 or diem_Tk<0:
    print("diem khong hop le")
elif diem_Tk>= 0 and diem_Tk <= 3:
    print("loai kem")
elif diem_Tk> 3 and diem_Tk <= 4:
    print("loai yeu")
elif diem_Tk> 4 and diem_Tk <= 7:
    print("loai trung binh")
elif diem_Tk> 7 and diem_Tk <= 9:
    print("loai kha")
else:
    print("loai gioi")