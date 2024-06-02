import my_Triangle

def main():
    try:
        # Nhập các cạnh của tam giác từ bàn phím
        a = float(input("Nhập cạnh a: "))
        b = float(input("Nhập cạnh b: "))
        c = float(input("Nhập cạnh c: "))

        # Kiểm tra và tính toán
        if my_Triangle.is_TamGiac(a, b, c):
            print(f"Ba cạnh {a}, {b}, và {c} có thể tạo thành một tam giác.")
            print(f"Chu vi: {my_Triangle.ChuviTamGiac(a, b, c)}")
            print(f"Diện tích: {my_Triangle.S_TamGiac(a, b, c)}")
        else:
            print(f"Ba cạnh {a}, {b}, và {c} không thể tạo thành một tam giác.")
    except ValueError as e:
        print(f"Lỗi: {e}")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

if __name__ == "__main__":
    main()

