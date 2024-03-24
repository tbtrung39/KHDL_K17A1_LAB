n = int(input("Nhập một số nguyên dương n: "))
so_hoan_hao = []
for i in range(1, n):
    tong = 0
    for j in range(1, i):
        if i % j == 0:
            tong += j
    if tong == i:
        so_hoan_hao.append(i)
print(f"Các số hoàn hảo nhỏ hơn", n, "là:", so_hoan_hao)