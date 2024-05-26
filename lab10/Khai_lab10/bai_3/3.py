from package_3 import sohoc as s
a=int(input('nhập số thứ nhất:'))
b=int(input('nhập số thứ hai:'))
n=int(input('nhập số n:'))
print(f'bội chung nhỏ nhất của hai số {a} và {b} là: {s.BCNN(a,b)}')
print(f'ước chung lớn nhất của hai số {a} và {b} là: {s.UCLN(a,b)}')
print(f'tổng các ước của {n}: {s.SumDivisor(n)}')