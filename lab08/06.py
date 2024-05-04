def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def bcnn(a, b):
    ucln = ucln(a, b)
    return (a * b) // ucln
so_a = int(input("Nhập a: "))
so_b = int(input("Nhập b: "))
Bcnn = bcnn(so_a, so_b)
print( Bcnn)