import math

x = float(input("Nhập giá trị x: "))

log_4_x = math.log(x, 4)
log_x_2 = math.log(2, x)
result = log_4_x + log_x_2

print("Giá trị của biểu thức f(x) =", round(result, 2))
