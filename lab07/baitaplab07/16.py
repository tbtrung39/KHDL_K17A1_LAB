a = [1, 2, 3, 2, 4]
n = len(a)
pairs = []

for i in range(n):
    for j in range(i+1, n):
        if a[i] + 1 == a[j]:
            pairs.append((i, j))

print("Các cặp chỉ số (i, j) thỏa mãn điều kiện a[i] + 1 = a[j] là:")
for pair in pairs:
    print(pair)