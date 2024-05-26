from pk_10 import my_square, my_triangle

choice = input("Bạn muốn tính chu vi và diện tích của tam giác hay hình vuông? (tamgiac/hinhvuong): ").strip().lower()

if choice == "tamgiac":
    a = float(input("Nhập độ dài cạnh a: "))
    b = float(input("Nhập độ dài cạnh b: "))
    c = float(input("Nhập độ dài cạnh c: "))
    
    if my_triangle.is_TamGiac(a, b, c):
        print("Chu vi của tam giác là:", my_triangle.Chuvi_TamGiac(a, b, c))
        print("Diện tích của tam giác là:", my_triangle.S_TamGiac(a, b, c))
    else:
        print("Ba cạnh không tạo thành một tam giác.")
elif choice == "hinhvuong":
    a = float(input("Nhập độ dài cạnh a: "))
    print("Chu vi của hình vuông là:", my_square.ChuviHinhvuong(a))
    print("Diện tích của hình vuông là:", my_square.Dien_tich_hinh_vuong(a))
else:
    print("Lựa chọn không hợp lệ.")
