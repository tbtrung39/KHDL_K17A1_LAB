chuoi = input("Nhap mot chuoi ky tu : ")
result = 0 
for i in chuoi : 
    if i.isnumeric(): 
        result = result * 10 + int(i)
print(result)

# tim so hoan hao : 
sum = 1 
for j in range(2, result): 
    if result % j == 0 : 
        sum += j
if sum == result : 
    print(f"{result} la so hoan hao ")
else: 
    print(f"{result} khong phai so hoan hao ")
