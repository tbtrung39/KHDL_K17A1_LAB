n = int(input("Nhập số Fibonacci muốn hiển thị: "))
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib
dãy_fibonacci = fibonacci(n)
print(", ".join(str(số) for số in dãy_fibonacci))
