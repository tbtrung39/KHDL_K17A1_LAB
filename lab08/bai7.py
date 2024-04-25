def find_min(a, b, c):
    return min(a, b, c)

def find_max(a, b, c):
    return max(a, b, c)

def main():
    print("Nhập vào ba số nguyên:")
    a = int(input("Nhập số thứ nhất: "))
    b = int(input("Nhập số thứ hai: "))
    c = int(input("Nhập số thứ ba: "))

    min_number = find_min(a, b, c)
    max_number = find_max(a, b, c)

    print(f"Số nhỏ nhất là: {min_number}")
    print(f"Số lớn nhất là: {max_number}")

if __name__ == "__main__":
    main()