def in_uoc(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)
n = int(input("nhap so nguyen duong n: "))
if n < 0:
    print("loi!!!")
else: 
    in_uoc(n)