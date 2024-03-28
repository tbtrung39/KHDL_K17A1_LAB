n = int(input("Nhập số n: "))

list_num_hh = []
for num in range(1, n):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        list_num_hh.append(num)

print("Các số hoàn hảo nhỏ hơn", n, "là:", list_num_hh)
