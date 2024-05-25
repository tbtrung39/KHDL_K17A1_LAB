# Nhập số phần tử của dãy
j = int(input("Nhập số phần tử của dãy số (j): "))
sum = 1




n = 1
while n <= j:
    sum *= (2*n) / (2*n + 1)
    n += 1


sum = round(sum, 3)

print("Tổng của dãy số là:", sum)
