import math
x = float(input("Nhập giá trị x: "))
n = int(input("Nhập giá trị n: "))
x = x % (2 * 3.14)
ket_qua = 0
for i in range(0, n+1):
        ket_qua += ((-1) ** i) * (x**(2*i) / math.factorial(2*i))
print("giá tri cần tìm là: ", ket_qua)