#5ucln
def ucln(a,b):
    while b:
        a,b=b,a % b
    return a
so_a=int(input("moi nhap so a"))
so_b=int(input("moi nhap so b"))
uc_lon_nhat=ucln(so_a,so_b)
print("uoc chung lon nhat cua a va b la:",uc_lon_nhat)