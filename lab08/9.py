#9
def tinh_toan(a,b):
    cong=a+b
    tru=a-b
    nhan=a*b
    chia=a//b
    return cong,tru,nhan,chia
a=int(input("moi nhap so a:"))
b=int(input("moi nhap so b"))
thuc_hien_phep_tinh=tinh_toan(a,b)
print("so sau khi duoc thuc hien la:",thuc_hien_phep_tinh)