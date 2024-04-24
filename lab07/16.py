a = [2, 3, 5, 7, 8, 10, 12]  

pairs = [] 

n = len(a)
for i in range(n):
    for j in range(i+1, n):
        if a[i] + 1 == a[j]:
            pairs.append((i, j))
print(pairs)