n = int(input("Nhập một số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập lại, n phải là số nguyên dương.")
s4 = 0
i = 1
while i <= n:
    s4 += i ** 2
    i += 1
s5 = 0
i = 1
while i <= n:
    s5 += (2 * i + 1) ** 3
    i += 1
s6 = 0
i = 1
while i <= n:
    s6 += (2 * i) ** 4
    i += 2
print("Tổng s4:", s4)
print("Tổng s5:", s5)
print("Tổng s6:", s6)