num1 = int(input("\n Nhập số nguyên thứ nhất: "))
num2 = int(input("Nhập số nguyên thứ hai: "))
bcnn = max(num1, num2)
while True:
    if bcnn % num1 == 0 and bcnn % num2 == 0:
        print(f"BCNN của {num1} và {num2} là: {bcnn}")
        break
    bcnn += 1