from pk_b3 import sohoc
def main():
    a = int(input("Nhập giá trị a:"))
    b = int(input("Nhập giá trị b:"))
    n = int(input("Nhập giá trị n:"))
    ucln = sohoc.Ucln(a, b)
    print("Ước chung lớn nhất là:", ucln)
    bcnn = sohoc.Bcnn(a, b)
    print("Bội chung nhỏ nhất là:", bcnn)
    sum = sohoc.SumDivisor(n)
    print("Tổng các ước của n là:", sum)
if __name__ == "__main__":
    main()