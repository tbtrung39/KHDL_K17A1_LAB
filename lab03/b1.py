n = int(input("Nhập vào số nguyên dương n: "))

sum = 0
product = 1
for i in range(1, n+1):
    sum += product
    product *= (2*i) / (2*i + 1)
print("Kết quả của phép toán là:", round(sum, 3))