def is_triangle(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Các cạnh phải là số dương.")
        if a + b > c and a + c > b and b + c > a:
            return "Ba cạnh tạo thành tam giác."
        else:
            return "Ba cạnh không tạo thành tam giác."
    except ValueError:
        return "Giá trị nhập không hợp lệ, vui lòng nhập lại ba số dương."

# Nhập từ người dùng
a = input("Nhập cạnh a: ")
b = input("Nhập cạnh b: ")
c = input("Nhập cạnh c: ")

# Kiểm tra và in kết quả
print(is_triangle(a, b, c))