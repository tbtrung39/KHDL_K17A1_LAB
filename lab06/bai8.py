n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập số nguyên dương.")
else:
    fib = [0, 1]
    [fib.append(fib[-1] + fib[-2]) for _ in range(2, n)]
    print(", ".join(map(str, fib)))
