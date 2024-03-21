import math 
x = int(input("nhập giá trị của x:"))
tinh = (-x + math.sqrt((x**2)+4))/(((x**4)+1)**1/7)
print("kết quả", round(tinh,2))