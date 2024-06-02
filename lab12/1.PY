import math

def kiem_tra_tam_giac(a, b, c):
    return a + b > c and a + c > b and b + c > a

def s_tam_giac(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

while True:
    try:
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))

        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Phải lớn hơn 0.")

        if not kiem_tra_tam_giac(a, b, c):
            raise ValueError("ko là tam giác")

        dien_tich = s_tam_giac(a, b, c)
        print("S: ", dien_tich)
        break

    except ValueError as ve:
        print(f"Lỗi: {ve}")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")