a = [1, 2, 4]
lst_cap = [(i, j) for i in range(len(a) - 1) for j in range(i + 1, len(a)) if a[i] + 1 == a[j]]
print(f"Các cặp (i, j) thỏa mãn điều kiện a[i] + 1 = a[j] là: {lst_cap}")
