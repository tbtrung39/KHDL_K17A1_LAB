chuoi_W = input("Nhập chuỗi ký tự W: ")
tu_dien_kw = {}

for i in range(len(chuoi_W)):
    for j in range(i + 1, len(chuoi_W) + 1):
        tu = chuoi_W[i:j]
        tu_dien_kw[tu] = tu_dien_kw.get(tu, 0) + 1

print(f"Từ điển chứa các cặp (K, V) là: {tu_dien_kw}")
