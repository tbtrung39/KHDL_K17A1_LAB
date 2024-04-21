tu_dien= dict()
#b
while True:
    print("chuong trinh them thong tin sinh vien")
    ma_sv = str(input("nhap ma sinh vien: "))
    if len(ma_sv) != 6:
        print("ma sinh vien phai la 6 ki tu so")
        continue
    ten_sv = input("nhap ten sinh vien: ")
    diem_so= int(input("nhap diem: "))
    sinh_vien = {"name": ten_sv, "score": diem_so}
    tu_dien[ma_sv] = sinh_vien    
    hoi = input("co tiep tuc nhap thong tin khong? (yes/no): ")
    if hoi == "no":
        break
print(tu_dien)
tu_dien_sapxep = dict(sorted(tu_dien.items(), key=lambda x: x[1]["score"], reverse=True))
print(tu_dien_sapxep)