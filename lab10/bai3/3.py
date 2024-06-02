import sohoc

def main():
    try:
        a = int(input("Nhập số nguyên a: "))
        b = int(input("Nhập số nguyên b: "))

        gcd = sohoc.Ucln(a, b)
        lcm = sohoc.Bcnn(a, b)
        print(f"Ước chung lớn nhất (UCLN) của {a} và {b} là: {gcd}")
        print(f"Bội số chung nhỏ nhất (BCNN) của {a} và {b} là: {lcm}")

        n = int(input("Nhập số nguyên n: "))

        sum_divisors = sohoc.SumDivisor(n)
        print(f"Tổng các ước của {n} là: {sum_divisors}")

    except ValueError as e:
        print(f"Lỗi: {e}")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

if __name__ == "__main__":
    main()
