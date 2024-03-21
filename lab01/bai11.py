n = int(input("nhập vào số lần tung xúc sắc: "))
p = (1/6)**3
q = (1-p)**n
xx = 1 - q
print(f"xác suất số lần ra 3 con 6 khi tung {n} lần xúc sắc = {xx:.2f}")