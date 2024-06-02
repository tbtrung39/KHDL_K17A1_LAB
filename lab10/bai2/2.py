import my_square

def main():
    try:
        a = float(input("Nhập cạnh a của hình vuông: "))
        chu_vi = my_square.ChuviHinhvuong(a)
        dien_tich = my_square.Dien_tich_hinh_vuong(a)
        
        print(f"Chu vi của hình vuông có cạnh {a} là: {chu_vi}")
        print(f"Diện tích của hình vuông có cạnh {a} là: {dien_tich}")
        
    except ValueError as e:
        print(f"Lỗi: {e}")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

if __name__ == "__main__":
    main()
