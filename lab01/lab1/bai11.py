n = int(input("Nhập số lần tung xúc sắc : "))

a = (5/6) ** n

xx = 1 - a

print("Xác suất ít nhất 1 lần cả 3 xúc sắc ra số 6 sau", n, "lần tung là:", round(xx, 2))
