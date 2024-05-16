n = int(input("Nhập số tự nhiên n: "))

tong = 0
number = 2
print(f"Các số nguyên tố đầu tiên là:")
while tong < n:
    a = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            a = False
            break
    if a:
        print(number)
        tong += 1
    number += 1