# main.py

from package_2 import my_square

def main():
    # Đọc giá trị cạnh của hình vuông từ người dùng
    canh_hinh_vuong = float(input("Nhập độ dài cạnh của hình vuông: "))

    # Tính chu vi và diện tích
    chu_vi = my_square.chu_vi_hinh_vuong(canh_hinh_vuong)
    dien_tich = my_square.dien_tich_hinh_vuong(canh_hinh_vuong)

    # Hiển thị kết quả
    print(f"Chu vi của hình vuông là: {chu_vi}")
    print(f"Diện tích của hình vuông là: {dien_tich}")

if __name__ == "__main__":
    main()