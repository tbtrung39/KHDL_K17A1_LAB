n = int(input("Nhap so nguyen duong la:"))
S4 = 0
S5 = 0
S6 = 0
while n > 0:
    for i in range (1,n+1):
        S4 += i**2
        if i % 2 == 1:
            S5 += i**3
        if i % 2 == 0:
            S6 += i**4
    break
print("S4=",S4)
print("S5=",S5)
print("S6=",S6)