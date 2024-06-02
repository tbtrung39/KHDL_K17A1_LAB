A=[]
while True:
    n=int(input("Nhập sô nguyên n(Nhap 0 để dừng):"))
    if n==0:
        break
    A.append(n)
print("A:",A)
B=[i for i in A if i%3==0 and i%5!=0]
print("B:",B)
C=[i**i for i in A]
print("C:",C)  
D=[i for i in A if i%3==0]
print("D:",D)