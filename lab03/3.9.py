n = int(input("Nhập một số nguyên dương n: "))
if n <= 0:
    print("n phải là số nguyên dương. Vui lòng nhập lại.")
S4 = 0
for i in range(1, n + 1):
    S4 += i ** 2
S5 = 0
for i in range(1, 2 * n + 2, 2):
    S5 += i ** 3
S6 = 0
for i in range(2, 2 * n + 1, 2):
    S6 += i ** 4
print(f"Tổng S4 = {S4}")
print(f"Tổng S5 = {S5}")
print(f"Tổng S6 = {S6}")