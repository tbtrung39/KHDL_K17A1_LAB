n=int(input("nhap so tu nhien: "))
A=set()
for i in range(2,n+1):
    if n%i==0:
        la_nguyen_to=True
        for j in range(2, int(i**0.5)+1):
            if i% j ==0:
                la_nguyen_to=False
                break
        if la_nguyen_to:
            A.add(i)
B=set()
for i in range(2,n):
    if i not in A:
        B.add(i)

print(A)
print(B)    