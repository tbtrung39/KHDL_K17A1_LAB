n = int(input("Nhập một số tự nhiên: "))
a = {i for i in range(1, n+1) if n % i == 0}
b = {i for i in range(2, n) if all(i % j != 0 for j in range(2, int(i**0.5)+1)) and n % i != 0}
print("Tập hợp a:", a)
print("Tập hợp b:", b)