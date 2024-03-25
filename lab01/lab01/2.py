import math
x=float(input("nhap x:"))
bieu_thuc=(-x+math.sqrt(x**2+4))/((x**4+1)**1/7)
print(f"bieu_thuc={bieu_thuc:.2f}")