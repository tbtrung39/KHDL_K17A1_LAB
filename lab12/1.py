import math

def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

while True:
    try:
        a = float(input("Nhập độ dài cạnh a: "))
        b = float(input("Nhập độ dài cạnh b: "))
        c = float(input("Nhập độ dài cạnh c: "))

        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Các cạnh phải là số dương lớn hơn 0.")
        
        if not is_valid_triangle(a, b, c):
            raise ValueError("Ba cạnh không thỏa mãn điều kiện tồn tại tam giác.")

        area = triangle_area(a, b, c)
        print(f"Diện tích của tam giác là: {area:.2f}")
        break

    except ValueError as ve:
        print(f"Lỗi: {ve}")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")