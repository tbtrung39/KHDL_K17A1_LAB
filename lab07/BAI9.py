n = int(input("Nhập một số tự nhiên n: "))
tap_hop_A = {i for i in range(1, n + 1) if n % i == 0 and all(i % j != 0 for j in range(2, i))}
tap_hop_B = {i for i in range(1, n) if all(i % j != 0 for j in range(2, i))}

print("Tập hợp A:", tap_hop_A)
print("Tập hợp B:", tap_hop_B)