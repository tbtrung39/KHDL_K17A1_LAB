import module4

def main():
    try:
        print("Giải phương trình bậc nhất ax + b = 0")
        a = float(input("Nhập a: "))
        b = float(input("Nhập b: "))
        result = module4.giai_pt_bac_nhat(a, b)
        print(f"Kết quả: {result}")

        print("\nGiải phương trình bậc hai ax^2 + bx + c = 0")
        a = float(input("Nhập a: "))
        b = float(input("Nhập b: "))
        c = float(input("Nhập c: "))
        result = module4.giai_pt_bac_hai(a, b, c)
        print(f"Kết quả: {result}")

    except ValueError as e:
        print(f"Lỗi: {e}")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

if __name__ == "__main__":
    main()
