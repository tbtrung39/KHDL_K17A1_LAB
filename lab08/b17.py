def tong_cac_so_chan(n):
    s = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            s += i
    return s

n = int(input("Nhập số nguyên dương n là:"))
sum = tong_cac_so_chan(n)
print(f"Tổng các số chẵn từ 1 đến {n} là: ",sum)