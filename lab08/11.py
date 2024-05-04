#11
def tinh_diem_trung_binh(a,b,c):
    diem_tb=(a+b+c)//3
    return diem_tb
ten_sv=input("moi nhap ten sv:")
a=int(input("moi nhap diem toan cua sv:"))
b=int(input("moi nhap diem ly cua sv:"))
c=int(input("moi nhap diem hoa cua sv:"))
tinh_diem_trung_binh(a,b,c)
print("diem trung binh cac mon toan ly hoa cua sv la:",tinh_diem_trung_binh(a,b,c))

