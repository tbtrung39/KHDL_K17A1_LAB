n = int(input("Nhập số tự nhiên n: "))
print(f"{n} số nguyên tố đầu tiên là:")
count = 0
num = 2  # Bắt đầu từ số nguyên tố đầu tiên là 2
while count < n:
    nt = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            nt = False
            break
    if nt:
        print(num, end=" ")
        count += 1
    num += 1