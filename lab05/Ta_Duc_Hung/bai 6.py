import math
str = input("Nhập chuỗi: ")
ki_tu = '0123456789ABCDEF'
he_hex = ''.join(char for char in str if char in ki_tu)
he_10 = sum(int(x, 16) * math.pow(16, len(he_hex)-i-1) for i, x in enumerate(he_hex)) 
print("hệ 10 là: ", he_10) 