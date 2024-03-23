m = int(input("Nhap m la:"))
s1 = 0
s2 = 0
s3 = 0
while m > 0:
    for i in range(1,m+1):
        if i % 2 == 0:
            s1 -= 1/i
        if i % 2 == 1:
            s1 += 1/i
    for i in range(1,m):
        s2 += 1/(i*(i+1))
    for i in range(2,m+1):
        s3 += 1/(i**(1/2))
    break
print("s1=",s1)
print("s2=",s2)
print("s3=",s3)