import random
a = set()
n = int(input("Enter the number of in the set:"))
while len(a)<n:
    a.add(random.randint(0,100))
a1 = min(a)
a2 = max(a)
a3 = sum(a)
print(set(a))
print("min:",a1)
print("max:",a2)
print("sum:",a3)