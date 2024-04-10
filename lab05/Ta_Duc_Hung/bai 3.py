n = int(input("Nhập số thập phân: "))
he_so = ''
if n ==0:
    print("Số nhị phân là 0")
else:
    while n > 0:
        he_so = str(n % 2) + he_so
        n //=2
print("số nhị phân là: ",  he_so)