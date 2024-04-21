a = [1, 2, 4]
lst_cap = []
n = len(a)
for i in range(n - 1):
    for j in range(i + 1, n):
        if a[i] + 1 == a[j]:
            lst_cap.append((i, j))
print(f"Các cặp (i, j) thỏa mãn điều kiện a[i] + 1 = a[j] là: {lst_cap}")