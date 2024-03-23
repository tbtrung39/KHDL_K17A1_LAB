so_hoan_hao = int(input("nhập vào số nguyên n: "))
sum = 0
for i in range(1,so_hoan_hao):
    if so_hoan_hao % i == 0: 
        sum += i 
    if so_hoan_hao == sum : 
        print(f"{so_hoan_hao} là số hoàn hảo")
        break
else:
    print(f"{so_hoan_hao} ko phải số hoàn hảo")