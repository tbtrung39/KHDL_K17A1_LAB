import math

def tinh_dien_tich_tam_giac(a, b, c):
    s = (a + b + c) / 2
    dien_tich = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return dien_tich

try:
    a = float(input("Nhập độ dài cạnh a: "))
    b = float(input("Nhập độ dài cạnh b: "))
    c = float(input("Nhập độ dài cạnh c: "))

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Độ dài các cạnh phải là số dương.")
    elif a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Độ dài các cạnh không thỏa mãn điều kiện tồn tại tam giác.")

    dien_tich = tinh_dien_tich_tam_giac(a, b, c)
    print("Diện tích tam giác là:", dien_tich)

except ValueError as ve:
    print("Lỗi:", ve)
except Exception as e:
    print("Lỗi không xác định:", e)
