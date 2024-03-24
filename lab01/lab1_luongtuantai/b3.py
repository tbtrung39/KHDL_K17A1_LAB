x=float(input("nhap so duong x: "))
import math
s=((-x)+math.sqrt(x**2+4))/(x**4+1)**(1/7)
s=round(s,2)
print("gia tri cua bieu thuc la: ",s)