#a
tu_dien= dict()
#b
while True:
    print("chuong trinh them thong tin nhan vien")
    ma_nv = input("nhap ma nhan vien: ")
    ten_nv = input("nhap ten nhan vien: ")
    nam_sinh= int(input("nhap nam sinh: "))
    luong = int(input("nhap tien luong: "))
    hoi = input("co tiep tuc nhap thong tin khong? (yes/no): ")
    tu_dien.update({ma_nv : [ten_nv,nam_sinh,luong]})
    if hoi == "no":
        break
print(tu_dien)
#c
x = input("nhap ma nhan vien can tim: ")
print(tu_dien[x])
#d
y = input("nhap ma nhan vien muon tang luong: ")
tu_dien[y][2]+= 100000
print(tu_dien[y])
#e
z= input("nhap ma nhan vien muon xoa: ")
if z in tu_dien:
    del tu_dien[z]
    print("Đã xóa thông tin của nhân viên có mã:", z)
else:
    print("Mã nhân viên không tồn tại.")
#f
tu_dien_sapxep = dict(sorted(tu_dien.items(), key=lambda x: x[1][1], reverse=True))
print(tu_dien_sapxep)
