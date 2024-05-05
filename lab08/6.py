def tim_ucln(a,b):
    while b:
        a,b = b,a%b
        return a
def tim_bcnn(a,b):
    return abs(a * b)// tim_ucln(a,b)

a = int(input('Nhập a:'))
b = int(input('Nhập b:'))
BCNN = tim_bcnn(a,b)
print(f'Bội chung nhỏ nhất là: {BCNN}')