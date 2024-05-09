def uoc_chung(a, b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b
a = int(input('nhập vào tử số:'))
b = int(input('nhập vào mẫu số:'))
print('Uoc so chung lon nhat cua a va b la: ', uoc_chung(a, b))