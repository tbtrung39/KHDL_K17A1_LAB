n = int(input("Nhập số lượng số Fibonacci: "))
fibonacci = [
    0 if i == 0 else 
    1 if i == 1 else 
    fibonacci[i-1] + fibonacci[i-2] 
    for i in range(n)]
print("Dãy Fibonacci:", end=" ")
print(*fibonacci, sep=", ")