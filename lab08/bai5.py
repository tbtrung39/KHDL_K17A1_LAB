def ucln(a, b):
    while b:
        a, b = b, a%b
    return a
a=int(input("nhap a : "))
b=int(input("nhap b : "))
ucl=ucln(a,b)
print("ucln la:  ",ucl)
