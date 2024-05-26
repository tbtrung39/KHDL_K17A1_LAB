import hinhhoc
def main():
    a = float(input("Nhap do dai canh a: "))
    b = float(input("Nhap do dai canh b: "))
    c = float(input("Nhap do dai canh c: "))
    if hinhhoc.is_TamGiac(a, b, c):
        print("Day la hinh tam giac")
        chu_vi = hinhhoc.Chuvi_TamGiac(a, b, c)
        print("Chu vi tam giac:", chu_vi)
        dien_tich = hinhhoc.S_TamGiac(a, b, c)
        print("Dien tich tam giac:", dien_tich)
    else:
        print("Day khong phai hinh tam giac")
    # Sử dụng module my_square.py
    a = float(input("Nhập cạnh của hình vuông: "))
    print(f"Chu vi hình vuông là: {hinhhoc.ChuviHinhvuong(a)}")
    print(f"Diện tích hình vuông là: {hinhhoc.Dien_tich_hinh_vuong(a)}")