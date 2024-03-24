a = list(map(float, input("Nhập vector a: ").split()))
b = list(map(float, input("Nhập vector b: ").split()))
tich = sum(map(lambda x, y: x * y, a, b))
print("Tích vô hướng của hai vector là:", tich)