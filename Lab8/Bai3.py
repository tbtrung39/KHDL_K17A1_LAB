def snt(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    n = int(input("Nhập số nguyên n: "))
    for so in range(2, n):
        if snt(so):
            print(so, end=" ")
