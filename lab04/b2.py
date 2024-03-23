n= int(input("nhap n: "))
S1=0
S2=0
S3=0
i=1
while i <=n:
    if i % 2 !=0:
        S1+=1/i
    else:
        S1-=1/i
    S2+= 1/(i*(i+1))
    i+=1
    S3+= 1/(i**0.5)

print("S1=",S1)
print("S2=",S2)
print("S3=",S3)