# File sử dụng module: main.py

from package_3 import sohoc

def main():
    a = int(input("Nhập số nguyên a: "))
    b = int(input("Nhập số nguyên b: "))
    n = int(input("Nhập số nguyên n: "))

    ucln = sohoc.ucln(a, b)
    bcnn = sohoc.bcnn(a, b)
    sum_divisors = sohoc.sumDivisor(n)

    print(f"Ước chung lớn nhất của {a} và {b} là: {ucln}")
    print(f"Bội số chung nhỏ nhất của {a} và {b} là: {bcnn}")
    print(f"Tổng các ước của {n} là: {sum_divisors}")

if __name__ == "__main__":
    main()

