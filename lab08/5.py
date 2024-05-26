def ucln(a,b):
    while b:
        a,b=b,a%b
    return a
a=int(input("Nhập a:"))
b=int(input("Nhập b:"))
print(f"UCLN của {a},{b} :",ucln(a,b))
