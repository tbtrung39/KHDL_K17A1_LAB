import math
x=input("Nhap gia tri cua x :")
x=float(x)
fx=(-x+math.sqrt(x**2+4))/((x**4+1)**(1/7))
print(f"Gia tri cua bieu thuc la :{fx:.2f}")