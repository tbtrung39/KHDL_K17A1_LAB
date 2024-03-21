n = int(input("Nhập số lần tung xúc sắc (n): "))

p = 5 / 6
p1 = p ** n
result = round(1 - p1, 2)

print(f"Xác suất ít nhất 1 lần cả 3 xúc sắc đều ra số 6 sau {n} lần tung là: {result}")