m = int(input("Nhap m la:"))
s4 = 0
s5 = 0
s6 = 0
while m > 0:
    for i in range(1,m+1):
        s4 += i**2
    for i in range(1,m+1):
        if i % 2 != 0:
            s5 += i**3
    for i in range(2,m+1):
        if i % 2 == 0:
            s6 += i**4
    break
print("s4=",s4)
print("s5=",s5)
print("s6=",s6)