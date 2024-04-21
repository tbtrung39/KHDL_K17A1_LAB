n = int(input("Nhập số tự nhiên n: "))

A = {i for i in range(1, n+1) if n % i == 0 and all(i % j != 0 for j in range(2, int(i**0.5) + 1))}

B = {i for i in range(2, n) if all(i % j != 0 for j in range(2, int(i**0.5) + 1))}

# In kết quả
print("Tập hợp A:", A)
print("Tập hợp B:", B)
