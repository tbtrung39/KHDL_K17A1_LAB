n = int(input("nhập vào số nguyên tố n: "))
sum = 0
for i in range(0,n+1):
    sum += i**3
print(sum)