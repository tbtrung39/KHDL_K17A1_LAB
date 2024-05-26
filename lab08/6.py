def ucln(a,b):
    while b:
        a,b=b,a%b
    return a
def bcnn(a,b):
    return(a*b)//ucln(a,b)
a=int(input("Nhập a:"))
b=int(input("Nhập b:"))
print(f"BCNN của {a},{b} :",bcnn(a,b))
