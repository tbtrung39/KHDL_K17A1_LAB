n = int(input("Nhập n: "))
fib = [0, 1]
[fib.append(fib[-1] + fib[-2]) for _ in range(2, n)]
fib_str = ", ".join(map(str, fib))
print(fib_str)
