import random

lisst = [] 
A = []
for i in range(1, 100000): 
    lisst.append(i)
A.append(random.sample(lisst, 1000))
print("day list A la : ", A)