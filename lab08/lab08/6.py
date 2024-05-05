def tim_ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def tim_bcnn(a, b):
    return (a * b) // tim_ucln(a, b)
a = int(input("nhap so thu nhat: "))
b = int(input("nhap so thu hai: "))
bcnn = tim_bcnn(a, b)
print("Bội chung nhỏ nhất của", a, "và", b, "là:", bcnn)
