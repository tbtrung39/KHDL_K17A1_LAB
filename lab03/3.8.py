n = int(input("Nhập một số nguyên dương n: "))
if n <= 0:
    print("n phải là số nguyên dương. Vui lòng nhập lại.")
S1 = 0
for i in range(1, n + 1):
    S1 += i
S2 = 0
for i in range(1, 2 * n + 2, 2):
    S2 += i
S3 = 0
for i in range(2, 2 * n + 1, 2):
    S3 += i
print(f"Tổng S1 = {S1}")
print(f"Tổng S2 = {S2}")
print(f"Tổng S3 = {S3}")
