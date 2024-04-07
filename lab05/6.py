import math
str = input("Nhập chuỗi str tu bàn phím là: ")
chuoi_he_hex = '0123456789ABCDEF'
he_hex = ''.join(char for char in str if char in chuoi_he_hex)
chuyen_doi = sum(int(x, 16) * math.pow(16, len(he_hex)-i-1) for i, x in enumerate(he_hex)) 
print("Chuỗi sau khi chuyển đổi là: ", chuyen_doi)