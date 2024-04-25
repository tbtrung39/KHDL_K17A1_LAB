def la_so_nguyen_to(num):
    """Kiểm tra xem một số có phải là số nguyên tố hay không."""
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def in_so_nguyen_to_nho_hon_n(n):
    """In ra các số nguyên tố nhỏ hơn n."""
    print("Các số nguyên tố nhỏ hơn", n, "là:")
    for num in range(2, n):
        if la_so_nguyen_to(num):
            print(num)

n = int(input("Nhập một số nguyên dương n: "))
in_so_nguyen_to_nho_hon_n(n)