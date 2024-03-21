n = int(input("Nhập vào số nguyên n: "))
tong = 0
for i in range(1,n):
    if n % i == 0: 
        tong += i 
    if n == tong : 
        print(f"{n} là số hoàn hảo")
        break
else:
    print(f"{n} ko phải số hoàn hảo")