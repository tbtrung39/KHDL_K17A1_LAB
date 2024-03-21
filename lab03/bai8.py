n = int(input("Nhập số nguyên dương n: "))
S4 = 0
S5 = 0
S6 = 0
if n <= 0:
    print("n phải là số nguyên dương.")
else:
    # Tính tổng S4
    
    for i in range(1,n+1):
        S4 += i**2
    print("a) Tổng S4 =", S4)
    
    # Tính tổng S5
    for i in range(1, n + 1, 2):
        S5 += (2*i + 1)**3
    print("b) Tổng S5 =", S5)
    
    # Tính tổng S6
    for i in range(2, n + 1, 2):
        S6 += (2*i)**4
    print("c) Tổng S6 =", S6)