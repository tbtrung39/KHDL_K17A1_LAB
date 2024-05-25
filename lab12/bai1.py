def tinh_dien_tich(a, b, c):
    if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("tam giac khong ton tai")
    p = (a + b + c) / 2
    dien_tich = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return dien_tich

try:
    a = float(input("nhap do dai canh a: "))
    b = float(input("nhap do dai canh b: "))
    c = float(input("nhap do dai canh c: "))

    dien_tich = tinh_dien_tich(a, b, c)
    print("Diện tích tam giác là:", dien_tich)
except ValueError:
    print("Lỗi:")
except Exception:
    print("Lỗi:")
