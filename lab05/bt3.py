a = int(input("Nhập số tự nhiên: "))
so_nhi_phan = ""
print(f"Số {a} chuyển sang hệ nhị phân là: ",end="")
while a > 0:
    so_du = a % 2
    so_nhi_phan = str(so_du) + so_nhi_phan
    a //= 2
print(so_nhi_phan)