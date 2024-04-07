n = int(input("Nhap chuoi:"))
a = ''
while n > 0:
    a = str (n % 2) + a
    n //= 2
print("So nhi phan cua ",n , "la",a)