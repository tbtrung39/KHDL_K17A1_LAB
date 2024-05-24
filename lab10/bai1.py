from package_1 import my_Triange
def main():
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))

    if my_Triange.is_tam_giac(a, b, c):
        print(f"{a}, {b}, {c} tạo thành một tam giác.")
        chuvi = my_Triange.chu_vi_tam_giac(a, b, c)
        dientich = my_Triange.S_tam_giac(a, b, c)
        print(f"Chu vi tam giác: {chuvi}")
        print(f"Diện tích tam giác: {dientich}")
    else:
        print(f"{a}, {b}, {c} không tạo thành một tam giác.")

if __name__ == "__main__":
    main()