n = 0
while n <= 0:
    n = int(input("Nhập vào một số nguyên dương n: "))
    if n <= 0:
        print("Vui lòng nhập lại số nguyên dương.")

S4 = 0
i = 1
while i <= n:
    S4 += i**2
    i += 1

print("Tổng S4 =", S4)

S5 = 0
i = 1
while i <= n:
    S5 += (2*i + 1)**3
    i += 1

print("Tổng S5 =", S5)
 
S6 = 0
i = 1
while i <= n:
    S6 += (2*i)**4
    i += 1
print("Tổng S6 =", S6)
