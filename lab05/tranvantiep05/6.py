import math
chuoi = input("Nhap chuoi ky tu : ")
ki_tu = '0123456789ABCDEF'
he_hex = ''.join(char for char in chuoi if char in ki_tu)
he_10 = sum(int(x, 16) * math.pow(16, len(he_hex)-i-1) for i, x in enumerate(he_hex)) 
print("hệ 10 là: ", he_10) 