n = int(input("Nhập số nguyên n: "))
A = set()
for i in range(2, n + 1):
    if n % i == 0:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            A.add(i)
B = set()
for i in range(2, n):
    if n%i != 0:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            B.add(i)
print("tập A là ",A)
print("tập B là ",B)