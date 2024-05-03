def chu_vi(r):
    C = 2 * 3.14 * r
    return C
def dien_tich(r):
    S = 3.14 * r ** 2
    return S
r = int(input("Nhập bán kính: "))
C = chu_vi(r)
S = dien_tich(r)
print("Chu vi của hình tròn là:", C)
print("Diện tích của hình tròn là:", S)