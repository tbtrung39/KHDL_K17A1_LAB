a = int(input('Nhập a: '))
b = int(input('Nhập b: '))
def UCLN(a,b):
    while a!=b:
        if a > b:
            a = a-b
        else:
            b = b-a
    return a
def BCNN(a,b):
    bcnn = (a*b)/UCLN(a,b)
    return bcnn
print(f'bội chung nhỏ nhất của {a} và {b} là: {BCNN(a,b)}')