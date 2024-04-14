import random as r
a=[]
for i in range(0,1000):
    b=r.randint(1,99999)
    a.append(b) 
print(a)
#sử dụng hàm sort
a.sort()
print(a)
#không sử dụng sort
n = len(a)
for i in range(len(a)-1):
    for j in range(0, len(a)-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]