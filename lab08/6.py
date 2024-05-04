# 6 bcln
def ucln(a,b):
    while b:
        a,b=b,a%b
    return a
def bcnn(a,b):
    return (a*b)//ucln(a,b)
so_a=int(input("moi nhap so nguyen a"))
so_b=int(input("moi nhap so nguyen b"))
bc_nho_nhat=bcnn(so_a,so_b)
print("boi chung nho nhat cua a va b la:",bc_nho_nhat)

