def tim_ucln(a,b):
    while b:
        a ,b = b,a % b 
    return a
a = int(input('Nhập a:'))
b = int(input('Nhập b:'))
UCLN = tim_ucln(a,b)
print(f'Ước chung lớn nhất là: {UCLN}')