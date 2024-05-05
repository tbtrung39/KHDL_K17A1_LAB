a=int(input("Nhập số"))
b=int(input("Nhập số"))
def USCLN_1(a, b):
    if b == 0:
        return a
    return USCLN_1(b, a % b)

print('Uoc so chung lon nhat cua a va b la: ', USCLN_1(a, b))