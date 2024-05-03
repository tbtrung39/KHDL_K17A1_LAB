def max_min(a,b,c):
    ln = max(a,b,c)
    nn = min(a,b,c)
    return ln , nn
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
ket_qua = max_min(a,b,c)
print(f"Số lớn nhất và nhỏ nhất lần lượt là {ket_qua}")