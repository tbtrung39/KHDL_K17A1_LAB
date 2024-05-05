def cong(a,b):
    return a+b
def tru(a,b):
    return a-b
def nhan(a,b):
    return a*b
def chia(a,b):
    if b==0:
        return False
    return a/b
a=float(input("nhap so a : "))
b=float(input("nhap so b : "))
print("cong = ",cong(a,b))
print("tru = ",tru(a,b))
print("nhan = ",nhan(a,b))
print("chia = ",chia(a,b))
