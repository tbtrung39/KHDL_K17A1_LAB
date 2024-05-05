def sv_score(t,h,l):
    diem_tb = (t + h +l)/3
    return diem_tb
name = input("nhap ten sinh vien: ")
t = int(input(f"nhap diem toan cua sinh vien {name}: "))
h = int(input(f"nhap diem hoa cua sinh vien {name}: "))
l = int(input(f"nhap diem ly cua sinh vien {name}: "))
sv_score(t,h,l)
print(f"diem trung binh cau sinh vien {name} la: {sv_score(h,t,l)}")