from pk_b4 import pt_bac1, pt_bac2
def main():
    a1 = float(input("Nhập hệ số a của phương trình bậc nhất: "))
    b1 = float(input("Nhập hệ số b của phương trình bậc nhất: "))
    print("Kết quả phương trình bậc nhất:", pt_bac1.giai_phuong_trinh_bac_nhat(a1, b1))

    a2 = float(input("Nhập hệ số a của phương trình bậc hai: "))
    b2 = float(input("Nhập hệ số b của phương trình bậc hai: "))
    c2 = float(input("Nhập hệ số c của phương trình bậc hai: "))
    print("Kết quả phương trình bậc hai:", pt_bac2.giai_phuong_trinh_bac_hai(a2, b2, c2))

if __name__ == "__main__":
    main()
