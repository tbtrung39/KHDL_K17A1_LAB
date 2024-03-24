import math

x = float(input("Nhập giá trị của x (trong đơn vị radian): "))
sai_num = 1e-4  
n = 0  
a = 1  

while True:
    total = ((-1) ** n) * (x ** (2 * n)) / math.factorial(2 * n)
    a += total
    
    if abs(total) < sai_num:
        break
    
    n += 1

print(f"Gần đúng của cos({x}) với sai số {sai_num} là: {a}")
