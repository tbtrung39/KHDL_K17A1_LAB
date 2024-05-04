def cong(a,b):
    return a+b
def tru(a,b):
    return a-b
def nhan(a,b):
    return a*b
def chia(a,b):
    if b==0:
        print("Không thể chia cho 0")
    else:
        return a/b
a=float(input("Nhập a:"))
b=float(input("Nhập b:"))
print("a+b",cong(a,b))
print("a-b",tru(a,b))
print("a*b",nhan(a,b))
print("a/b",chia(a,b))

