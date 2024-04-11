import random
a = [random.randint(1, 99999) for _ in range(1000)]
n = len(a)
for i in range(n):
    b = i
    for j in range(i + 1, n):
        if a[b] > a[j]:
            b = j
    a[i], a[b] = a[b], a[i]

print("Danh sách a đã sắp xếp không sử dụng hàm sorted():")
print(a[:10]) 
a_sorted = sorted(a)