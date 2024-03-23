n = int(input("Nhập vào một số nguyên dương n: "))
if n <= 0:
    print("Đã dừng chương trình.")
else:
    s1=0
    s2=0
    s3=0

    for i in range(1,n+1):
        s1+=i

    for i in range(1, 2*n+2,2):
        s2 += i

    for i in range(2, 2*n+1,2):
        s3 += i

    print("Tổng S4 =", s1)
    print("Tổng S5 =", s2)
    print("Tổng S6 =", s3)