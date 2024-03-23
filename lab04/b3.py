import math
x=float(input('nhập giá trị x:'))
n=int(input('nhập giá trị n:'))
x = x % (2 * 3.14)
gia_trị = 0
for i in range(0, n + 1):
        gia_trị += ((-1) ** i) * (x**(2*i) / math.factorial(2*i))
print("giá tri cần tìm là: ", gia_trị)