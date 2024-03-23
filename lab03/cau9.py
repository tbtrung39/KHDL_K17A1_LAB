n = int(input("Nhập vào một số nguyên dương n: "))
if n <= 0:
    print("Đã dừng chương trình.")
else:
    s4=0
    s5=0
    s6=0

    for i in range(1,n+1):
        s4+=i**2

    for i in range(1, 2*n+2,):
        s5 += i**3

    for i in range(2, 2*n+1,):
        s6 += i**4

    print("Tổng S4 =", s4)
    print("Tổng S5 =", s5)
    print("Tổng S6 =", s6)