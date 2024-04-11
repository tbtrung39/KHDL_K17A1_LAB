import random
A=[]
n=int(input("nhap n so nguyen muon nhap: "))
for i in range (1,n+1):
    m= int(input("nhap so tu nhien: "))
    A.append(m)
print('list A:', A)
B=[x for x in A if x%3==0 and x% 5!=0]
print('list B:', B)
C=[x**2 for x in A]
print('list C:', C)
D = [x for x in random.sample(A, len(A)) if x % 3 == 0]
print('list D:', D)