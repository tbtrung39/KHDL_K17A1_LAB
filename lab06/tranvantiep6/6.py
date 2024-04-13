import random

lisst = [] 
A = []
for i in range(1, 100000): 
    lisst.append(i)
A.extend(random.sample(lisst, 1000))
print("day list A la : ", A)
# sap xep tang dan cach 1 : 
cach1 = sorted(A)
print("sap xep tang dan cach 1 : ", cach1)
# cach 2 ; 
A.sort()
print("sap xep tang dan theo cach 2 : ", A)