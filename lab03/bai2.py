n = int(input("nhập vào số nguyên n: "))
sum = 0
for i in range(1,n):
    if n % i == 0: 
        sum += i 
    if n == sum : 
        print(f"{n} là số hoàn hảo")
        break
else:
    print(f"{n} ko phải số hoàn hảo")