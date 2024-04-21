sv={}
n=int(input("Nhap so luong sinh vien:"))
for i in range(n):
    msv=int(input(f"Nhap ma sinh vien(6 so) cua sinh vien {i+1}:"))
    msv=str(msv)
    while len(msv) != 6:
        print("Ma sinh vien can phai la 6 so")
        msv =int(input("Nhap lai ma sinh vien:"))
        msv=str(msv)
    ten=str(input(f"Nhap ho va ten thi sinh so{i+1}:"))
    diem=float(input(f"Nhap diem thi thi sinh{i+1}:"))
    sv[msv] = {"Ho va ten":ten,"diem thi":diem}
