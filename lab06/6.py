import random
slg = 1000
list_A = []
for j in range(slg):
    s = random.randint(1, 99999)
    list_A.append(s)
print(sorted(list_A))