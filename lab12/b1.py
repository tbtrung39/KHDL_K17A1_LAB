import math

while True:
    try:
        a = int(input("Nhap canh thu nhat: "))
        b = int(input("Nhap canh thu hai la: "))
        c = int(input("Nhap canh thu ba la: "))
        if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
            raise ValueError
        p = (a + b + c) / 2
        S = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("Dien tich tam giac la:", S)
        break
    except ValueError:
        print("Sai, vui long nhap lai.")