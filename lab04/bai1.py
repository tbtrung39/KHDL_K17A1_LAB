n = int(input("Nhập vào một số nguyên dương(n>0): "))
while n <= 0:
    n = int(input("Vui lòng nhập lại n : "))
S4 = 0
S5=0
S6=0
i = 0
while i <= n:
    S4 += i**2
    S5 +=(2*i+1)**3
    S6+=(2*i)**4
    i += 1
print(" S4 =", S4)
print(" S5 =", S5)
print(" S6 =", S6)