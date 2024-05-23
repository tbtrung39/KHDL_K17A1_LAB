from pk1 import my_Triange

a, b, c = 3, 4, 5

# Gọi hàm kiểm tra tam giác
is_tamgiac = my_Triange.is_TamGiac(a, b, c)
print(f"Ba cạnh {a}, {b}, {c} có tạo thành tam giác không? {is_tamgiac}")

# Gọi hàm tính chu vi tam giác
chu_vi = my_Triange.ChuviTamGiac(a, b, c)
if chu_vi is not None:
    print(f"Chu vi tam giác là: {chu_vi}")

# Gọi hàm tính diện tích tam giác
dien_tich = my_Triange.S_TamGiac(a, b, c)
if dien_tich is not None:
    print(f"Diện tích tam giác là: {dien_tich}")
