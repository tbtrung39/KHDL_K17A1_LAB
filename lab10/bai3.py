import sys
sys.path.append("lab10\package_3")

import package_3
a=(int(input("nhap so duong a: ")))
b=(int(input("nhap so duong b: ")))
n=(int(input("nhap so duong n: ")))
print('BCNN cua a va b la: ',package_3.bcnn(a,b))
print('UCLN cua a va b la: ',package_3.ucln(a,b))
print("tong uoc cua n la:", package_3.sundivisor(n))