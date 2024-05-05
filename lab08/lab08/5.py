def tim_ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
a=int(input("nhap so thu nhat:"))
b=int(input("nhap so thu hai:"))
ucln=tim_ucln(a,b)
print("uoc chung lon nhat cua",a,"va",b,"la",ucln)