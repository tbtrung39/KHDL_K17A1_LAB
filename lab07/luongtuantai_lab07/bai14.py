dict_m = {}
for n in range(1, 101):
    dict_m[n] = bin(n)[2:]
for i, j in dict_m.items():
    print(i, ":", j)
print(f"Từ điển chứa cặp số từ 1 đến 100 và chuỗi nhị phân tương ứng là: {i} ':' {j}")