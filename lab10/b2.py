from pk_b2 import my_square
def main():
    a = float(input("Nhập độ dài cạnh a:"))
    chu_vi = my_square.Chuvihinhvuong(a)
    print("Chu vi hình vuông là:", chu_vi)
    dien_tich = my_square.Dien_tich_hinh_vuong(a)
    print("Diện tích hình vuông là:", dien_tich)
if __name__ == "__main__":
    main()