ttnv={}
n=int(input("Nhap so luong nhan vien:"))
#A,B
for i in range(n):
    mnv=int(input(f"Nhap ma nhan vien(4 so) cua sinh vien {i+1}:"))
    mnv=str(mnv)
    while len(mnv) != 4:
        print("Ma sinh vien can phai la 4 so")
        mnv =int(input("Nhap lai ma nhan vien:"))
        mnv=str(mnv)
    ten=str(input(f"Nhap ho va ten nhan vien so {i+1}:"))
    tuoi=int(input(f"Nhap nam sinh nhan vien so {i+1}:"))
    luong=int(input(f"Nhap luong nhan vien so {i+1}:"))
    ttnv[mnv] = {"Ho va ten":ten,"Nam sinh":tuoi,"luong":luong}
#C
tim_kiem=input("Nhap ma nhan vien:")
if tim_kiem in ttnv:
    nv= ttnv[tim_kiem]
    print("Thong tin nhan vien:")
    print(f"Ma nhan vien: {tim_kiem}")
    print(f"Ten nhan vien: {nv["ten"]}")
    print(f"Nam sinh: {nv["tuoi"]}")
    print(f"Luong: {nv["luong"]}")
else:
    print("Khong ton tai")
#D
tang_luong = input("Nhan vien duoc tang luong:")
if tang_luong in ttnv:
    ttnv[tang_luong]["luong"] +=1000000
    print(f"Luong moi cua {tang_luong} la: {ttnv[tang_luong]["luong"]}")
    print(f"Thong tin sau khi tang luong la:{ttnv}")
else:
    print("Khong ton tai")
#E
loai_bo=int(input("Ma nhan vien can xoa:"))
if loai_bo in ttnv:
    ttnv.pop(loai_bo)
    print(f"Nhan vien {loai_bo} da duoc xoa khoi danh sach")
    print(f"Thong tin sau khi loai bo la:{ttnv}")
else:
    print("Khong ton tai")



