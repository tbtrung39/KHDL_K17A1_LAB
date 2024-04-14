import random
A=[]
for i in range(1000):
    A.append(random.randint(1,9999))
print("sap xep theo thu tu tand dan bang sorted:", sorted(A))

n=len(A)
for i in range(n):
    for j in range(0,n-i-1):
        if A[j] > A[j+1]:
            A[j] = A[j+1]
print(A)