def tim_dinh_phuong_trinh_bac_2(a, b, c):
    # Tìm hoành độ của đỉnh
    x_v = -b / (2 * a)
    return x_v

def main():
    # Nhập giá trị a, b, c từ bàn phím
    a = float(input("Nhập giá trị của a: "))
    b = float(input("Nhập giá trị của b: "))
    c = float(input("Nhập giá trị của c: "))

    # Tìm đỉnh của phương trình bậc 2
    dinh = tim_dinh_phuong_trinh_bac_2(a, b, c)

    # In kết quả
    print("Đỉnh của phương trình bậc 2 là:", round(dinh, 2))

if __name__ == "__main__":
    main()
