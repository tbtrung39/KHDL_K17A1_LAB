n = int(input("Nhập số n: "))
chuoi_nhi_phan = ""
while n > 0:
    chuoi_nhi_phan = str(n % 2) + chuoi_nhi_phan
    n //= 2
print("Số nhị phân là:", chuoi_nhi_phan)
