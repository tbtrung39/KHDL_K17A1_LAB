W = input("Nhập chuỗi ký tự W: ")
dict_kw = {}
for i in range(len(W)):
    for j in range(i + 1, len(W) + 1):
        chx = W[i:j]
        if chx in dict_kw:
            dict_kw[chx] += 1
        else:
            dict_kw[chx] = 1
print(f"Từ điển chứa các cặp (K, V) là: {dict_kw}")