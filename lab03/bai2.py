n = int(input("Nhập một số nguyên dương n: "))

cac_so_hoan_hao = []
for i in range(1, n):
    tong_uoc = 0
    for j in range(1, i):
        if i % j == 0:
            tong_uoc += j
    if tong_uoc == i:
        cac_so_hoan_hao.append(i)

print("Các số hoàn hảo nhỏ hơn", n, "là:", cac_so_hoan_hao)
