n = int(input("Nhập số nguyên n: "))
a = [i for i in range(n)]
cap_so = []
for i in range(n - 1):
    for j in range(i + 1, n):
        if a[i] + a[j] == a[i + 1]:
            cap_so.append((i+1, j+1))
print("Các cặp chỉ số thỏa mãn điều kiện ai + aj = ai+1 là:")
for cap in cap_so:
    print(cap)
