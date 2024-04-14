# Nhập n từ bàn phím
n = int(input("Nhập n: "))

# Khởi tạo dãy Fibonacci với hai phần tử đầu tiên
fib = [0, 1]

# Tạo dãy Fibonacci với n phần tử
[fib.append(fib[-1] + fib[-2]) for _ in range(2, n)]

# In dãy Fibonacci dưới dạng tách biệt bằng dấu ","
fib_str = ", ".join(map(str, fib))
print(fib_str)
