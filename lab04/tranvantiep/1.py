#a
n = int(input("Nhap n : "))
if n <= 0 : 
    print("Moi nhap lai ")
else: 
    tong = 0 
    i = 1 
    while i <= n : 
        tong += i ** 2 
        i += 1
    print(tong)

# b 
n = int(input("Nhap n : "))
if n <= 0 : 
    print("MOi nhap lai ")
else :
    s5 = 0 
    i = 1
    while i <= n : 
        s5 += (2 * i + 1)**3
        i += 1 
    print(s5)

# c 
n = int(input("Nhap n : "))
if n <= 0 : 
    print("MOi nhap lai ")
else: 
    s6 = 1
    i = 1 
    while i <= n : 
        s6 += (2 * i)**4
        i += 1
    print(s6)