#câu 8:
n = int(input("Nhập số lượng số Fibonacci muốn tạo: "))
fibonacci = []

# Tạo dãy Fibonacci
a, b = 0, 1
for _ in range(n):
    fibonacci.append(a)
    a, b = b, a + b

# In dãy Fibonacci
print("Dãy số Fibonacci:")
print(fibonacci)
try:
    n = int(input("nhập vào dãy số fibonacci: "))
    for i in fibonacci:
        if n != i:
            print("không phải dãy fibonacci")
            print("vui lòng nhập dãy fibonacci")
            break
        else:
            print(n)
            n = str(n)
            b = ","
            a = [''.join(b) for b in n ]
            print(f"dãy số fibonacci tách biệt là {a}")
except ValueError:
        print("vui lòng nhập dãy fibonacci")
