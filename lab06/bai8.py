n = int(input("Nhập số n: "))
fibonacci = [0, 1] if n > 1 else [0] if n == 1 else []
[fibonacci.append(fibonacci[-1] + fibonacci[-2]) for i in range(2, n+1)]
chuoi_fibonancci = ', '.join(map(str, fibonacci))
print("Dãy Fibonacci đến số", n, "là:", chuoi_fibonancci)