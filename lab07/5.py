import random
ds = set(range(10))
A = set()
n = 5
phan_tu = random.sample(sorted(ds), n)  
A.update(phan_tu) 
print(A)