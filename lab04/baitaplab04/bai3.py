import math
x = math.pi / 4
sai_so = 1e-4

result = 1  
a = 1    

n = 2     

while abs(a) >= sai_so:  
    a = (-1) * a * x * x / (n * (n - 1))  
    result += a
    n += 2

print("Giá trị gần đúng của cos({}) là: {}".format(x, result))
print("Giá trị thực của cos({}) là: {}".format(x, math.cos(x)))
print("Sai số: {}".format(abs(math.cos(x) - result)))