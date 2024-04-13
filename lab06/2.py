import random
n=int(input("nhap gia tri n: "))
list=[]
for i in range(n):
    j=random.randint(-100,100)
    list.append(j)
print(list)
a=sorted(list)
a.remove()
print(a[1])
tong=0
for k in a:
    if k>0:
        tong+=k
print(tong)