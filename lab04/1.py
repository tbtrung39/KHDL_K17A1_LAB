n=int(input("mời bạn nhập số nguyên dương "))
S4 = 0
i = 1
while i <= n:
    S4 += i ** 2
    i += 1
print(S4)
S5 = 0
i = 1
while i <= n:
    S5 += (2 * i + 1) ** 3
    i += 1
print(S5)
S6 = 0
i = 2
while i <= 2 * n:
    S6 += i ** 4
    i += 2
print(S6)   

