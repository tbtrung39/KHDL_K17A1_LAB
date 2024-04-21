a = [1, 2, 3, 2, 4]
n = len(a)

cap_chi_so = []
for i in range(n - 1):
    for j in range(i + 1, n):
        if a[i] + a[j] == a[j]:
            cap_chi_so.append((i + 1, j + 1))  # Thêm cặp chỉ số (i+1, j+1) vào danh sách
print("Các cặp chỉ số thỏa mãn điều kiện:")
for cap_chi_so in cap_chi_so:
    print(cap_chi_so)