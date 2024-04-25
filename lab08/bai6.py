def ucln(a, b):
    while b:
        a, b = b, a % b
    return a

def bcnn(a, b):
    return abs(a*b) // ucln(a, b)

# Hàm main để chạy chương trình
def main():
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    result = bcnn(a, b)
    print(f"Bội chung nhỏ nhất của {a} và {b} là: {result}")

if __name__ == "__main__":
    main()