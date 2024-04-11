# a. Nhập số tự nhiên n từ bàn phím
n = int(input("Nhập một số tự nhiên n: "))

# b. Tạo tập hợp A và B
tap_hop_A = {i for i in range(1, n + 1) if n % i == 0 and all(i % j != 0 for j in range(2, i))}
tap_hop_B = {i for i in range(1, n) if all(i % j != 0 for j in range(2, i))}

# In ra tập hợp A và B
print("Tập hợp A:", tap_hop_A)
print("Tập hợp B:", tap_hop_B)