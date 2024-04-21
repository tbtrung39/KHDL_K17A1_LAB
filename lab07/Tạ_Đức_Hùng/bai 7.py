import random 

scope = int(input("Nhap pham vi de sinh ra A va B : "))
A = set()
B = set()
 
for i in range(1, scope): 
    A.add(random.randint(1, scope))
    B.add(random.randint(1, scope))

genaral = A.intersection(B)

print("Phan tu chung cua A va B la : ", genaral)