n = int(input("Nhập số nguyên n: "))
dict_m = {}
for i in range(1, n + 1):
    dict_m[i] = i*i
print(f"Dictionary chứa các cặp (i, i*i) từ 1 đến {n} là: {dict_m}")