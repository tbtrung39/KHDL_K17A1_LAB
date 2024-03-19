import math
x=int(input("nhập giá trị: "))
ket_qua=(-x+math.sqrt(x**2+4))/(math.pow((x**4+1),1/7))
print(f"f(x)= {ket_qua:.2f}")