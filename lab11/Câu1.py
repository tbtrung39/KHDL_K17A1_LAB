def create_dict(n):
    return {i: i * i for i in range(1, n + 1)}

n = int(input("Nhập số nguyên n: "))
result = create_dict(n)
print(result)