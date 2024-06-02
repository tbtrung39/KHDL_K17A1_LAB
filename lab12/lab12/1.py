import math

while True:
    try:
        a = int(input("Nhập cạnh thứ nhất: "))
        b = int(input("Nhập cạnh thứ hai: "))
        c = int(input("Nhập cạnh thứ ba: "))

        if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Các cạnh không hợp lệ để tạo thành một tam giác.")

        p = (a + b + c) / 2
        S = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("Diện tích tam giác là:", S)
        break
    except ValueError as ve:
        print("Sai, vui lòng nhập lại. Lỗi:", ve)
