diem_tk = float(input("nhap diem tong ket:"))
if 0<=diem_tk<3.0:
    print("Loai kem")
elif 3.0<=diem_tk<5.0:
    print("Loai yeu")
elif 5.0<=diem_tk<7.0:
    print("Loai Trung Binh")
elif 7.0<=diem_tk<8.0:
    print("loai kha")
elif 8.0<=diem_tk<9.0:
    print("Loai gioi")
elif 9.0<=diem_tk<=10.0:
    print("Xuatsac")
else:
    print("error, please try again")