def bcnn(x,y):
    p = x * y
    while x != y:
        if x < y:
            y = y - x
        else:
            x = x - y
    return p // x
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
print(f"Bội chung nhỏ nhất của {a} và {b} là {bcnn(a,b)}")