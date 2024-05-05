def ucln(a, b):
    while b:
        a, b = b, a%b
    return a
def bcnn(a,b):
    return a*b//ucln(a,b)
a=int(input("nhap a : "))
b=int(input("nhap b : "))
print("boi chung nho nhat : ",bcnn(a,b))