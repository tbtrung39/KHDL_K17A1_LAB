def get_even_sum(n):
    even_sum = 0
    for num in range(1, n+1):
        if num % 2 == 0:
            even_sum += num
    return even_sum
n = int(input("Nhập số n: "))
even_sum = get_even_sum(n)
print(f"Tổng của các số chẵn trong danh sách từ 1 đến {n} là: {even_sum}")