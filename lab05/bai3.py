n = int(input("nhập số n:"))
so_nhi_phan = ""
while n > 0:
    so_nhi_phan = str(n%2) + so_nhi_phan
    n = n // 2
print(f"số nhị phân tương ứng là:{so_nhi_phan}")