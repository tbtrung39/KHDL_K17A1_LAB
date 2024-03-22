n = int(input("Nhập số nguyên dương: "))
s1 = 0
while n > 0:
    for i in range(1,n+1):
        if i % 2 == 0:
            s1 -= 1/i
        else: 
            s1 += 1/i
    break
print("S = ",s1)
s2 = 0
while n > 0:
    for i in range(1,n):
        s2 += 1/(i*(i+1))
    break
print("S = ",s2)
s3 = 0
while n > 0:
    for i in range(2,n+1):
        s3 += 1/(i**(1/2))
    break
print("S = ",s3)