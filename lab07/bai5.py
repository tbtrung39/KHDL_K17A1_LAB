import random
A = set()
while len(A) < 5:
    a = random.randint(0,10,)
    if a not in A:
        A.add(a)
print(A)