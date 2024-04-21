m = int(input("Nhập số nguyên m: "))
n = int(input("Nhập số nguyên n: "))
set_m = set(range(m, n + 1))
set_n = set(range(n, m - 1, -1))
ptc_set = set_m.intersection(set_n)
total = 0
for i in ptc_set:
    total += i
print(f"Tổng các số chung từ {m} đến {n} là {total}")
