def tim_boi_chung_nho_nhat(a, b):
    max_so = max(a, b)
    while True:
        if max_so % a == 0 and max_so % b == 0:
            boi_chung_nho_nhat = max_so
            break
        max_so += 1
    return boi_chung_nho_nhat
so1 = 12
so2 = 15
print(f"Bội chung nhỏ nhất của {so1} và {so2} là:", tim_boi_chung_nho_nhat(so1, so2))
